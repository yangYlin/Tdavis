

import requests
from urllib.parse import quote
import time
from random import sample,choice

import pymongo
import matplotlib.pyplot as plt #数据可视化
 
from pylab import mpl


# wordcloud词云

from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import jieba
from PIL import Image
import matplotlib.ticker as ticker#设置x轴区间宽度
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)








class CrawlProduct:
    def __init__(self,key_word="羽毛球拍",MgodbName="yu_mao_qiu_pai"):
        self.url = "https://ai.taobao.com/search/getItem.htm"
        self.key_word = key_word
        self.MgodbName=MgodbName
        
        self.parmas = {'_tb_token_': '353a8b5a1b773',
              '__ajax__': '1', 
              'pid': 'mm_10011550_0_0',
              'page': '1',
              'pageSize': '60', 
              'sourceId': 'search',
              'pageNav': 'false',
              'key': quote(self.key_word),
              'debug': 'false',
              'maxPageSize': '200',
              'npx': '50'}
        self.page_num =80
        #存放数据库结果
        self.result = []
        
        #代理出现网页，在我本机上5000端口，需先开启服务器
        self.proxy_pool_url='http://localhost:5000/random'
        

        #连接mongoDB
        MONGO_RUL='localhost'
        MONGO_DB='Badminton_racket'
        MONGO_COLLECTION=self.MgodbName
        client=pymongo.MongoClient(MONGO_RUL)
        db=client[MONGO_DB]
        self.products=db[MONGO_COLLECTION]
        
    #随机选择一个浏览器
    def select_user_agent(self):
        
        uas = [
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
            "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
            "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
            "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
            "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
            "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
            "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
            "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
        ]
        user=choice(uas)
        user_dict={}
        return user_dict
    #从代理池获取代理
    def get_proxy(self):
        try:
            response=requests.get(self.proxy_pool_url)
            if response.status_code==200:
                return response.text
        except ConnectionError:
            return None
    
    #请求页面
    def requests_one_page(self):
        
        proxy=self.get_proxy()
        proxies={
            'http':'http://'+proxy,
            'https':'https://'+proxy
            }
        
        for p in range(1, self.page_num+1):
            self.parmas['page'] = str(p)
            try :
                r = requests.get(self.url, headers=self.select_user_agent(),params=self.parmas)#proxies==proxies
            except requests.exceptions.ConnectionError as e:
                print(e.args)
            data = r.json()#转为json格式
            #print("data数据为：")
            #print(data)
            items = data['result']['auction']
            self.parse_one_page(items)
        
            print("page: {}".format(p))
            time.sleep(1)
        
    #解析页面
    def parse_one_page(self,items):
        for item in items:
            #print(item)
            
           # print("\n")
            product={
                
                'itemId':str(item['itemId']),
                'desc':item['description'],
                'location' : item['itemLocation'],
                'nick' :item['nick'],
                'picUrl' :item['picUrl'],
                'price' :str(item['price']) if 'price' in item else 'NULL',
                'realPrice' :str(item['realPrice']),
                'saleCount' :str(item['saleCount'])
                

                }
            #print(product)
            self.save_to_mongo(product)



    #保存数据
    def save_to_mongo(self,product):
        
        try:
            self.products.insert(product)
                #print("成功！")
        except Exception:
            print("保存数据失败！")


    #数据清理         
    def delet_repeat_items(self):
        patents = {}
        count = 0
        collection=self.products
        #从数据库中找出ID不为0的，即全部数据
        for patent_record in collection.find({"_id":{"$ne":0}}):
            
            if patent_record['itemId'] not in patents.keys():
                patents[patent_record['itemId']] = patent_record
            else:
                count += 1
                collection.delete_one({'itemId':patent_record['itemId']})
        print('删除重复项目：',count)
        
    #------------------------------------------------------------------------各省店铺数分析---------------------------------------------------------------
    def data_anlysis(self):
        results=self.products.find({'desc':{'$exists':True}})
        location_list=[]
        location_dict_list=[]#存储各省数目和名称的元组
        
        name_list=[]#省名
        num_list=[]#商家数目
        for result in results:
            #print(result['desc'])
            location=result['location'][0:2]#只提取省名，
            #print(type(location))
            location_list.append(location)
            #print(location)
            location_dict_stastic=self.stastic_location(location_list)
        print(location_dict_stastic)
        for key ,val in location_dict_stastic.items():
            location_dict_list.append((val,key))
            
        for item in location_dict_list:
            #print(type(i))
            print(item[0],item[1])

            #省太多，图像显示不美观，这里只统计商店数大于5的省会
            #if item[0]>=5:
            name_list.append(item[1])
            num_list.append(item[0])#水平柱状图可以查看全部
            
             #print(type(item[1]))
            '''
             从这里得到了item[0]为int类型 ,省卖羽毛球拍的商家数目
             item[1]为str类型 ,信息表示会商家所在省会

             '''

        #self.show_location_data(name_list,num_list)
        self.shui_ping_bar(name_list,num_list)
    def shui_ping_bar(self,name_list,num_list):
        # 先生成一个画布
        fig = plt.figure()
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        # 设置
        a=plt.barh(name_list,num_list,color='b')
        #shui_ping_autolabel(a)
        #plt.yticks(arange(len(num_list)), num_list)
        plt.xlabel(self.key_word+"店铺数量") # 指定x轴描述信息
        plt.ylabel(self.key_word+"商家所在地区")   # 指定y轴描述信息
        plt.title(self.key_word+"店铺数量各地区统计表")  # 指定图表描述信息
        
        plt.show()
        
    #添加商家地点信息
    def stastic_location(self,location_list):
        location_dict={}
        for i in location_list:
            
            if i in location_dict:
                
                location_dict[i]+=1
            else:
                
                location_dict[i]=1
        return location_dict


    #显示柱状上的数值
    def autolabel(self,rects):
        
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' %int(height))

    #数据可视化    
    def show_location_data(self,name_list,num_list):
        #zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        a=plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
        self.autolabel(a)
        plt.xticks(rotation=45)
        plt.xlabel(self.key_word+"商家所在省会")  # 指定x轴描述信息
        plt.ylabel(self.key_word+"店铺数量")  # 指定y轴描述信息
        plt.title(self.key_word+"各省统计表")  # 指定图表描述信息
        #plt.savefig(self.key_word+"各省统计表.png")
        plt.xticks(rotation=25)
        plt.show()

            

    #--------------------------------------------------------------------------各城市出售月总量-------------------------------------------------------------------

    def city_saleCount(self):
        results=self.products.find({'saleCount':{'$exists':True}})
        city_list=[]
        sale_Count_list=[]
        city_saleCount_dict={}
        city_saleCount_dict_list=[]
        city_list_sum=[]  #城市名
        city_sale_count_list=[] #城市出售额

        
        for result in results:
            city_length=len(result['location'])#只提取城市名，
            if city_length>2:
                city=result['location'][3:]
            else:
                city=result['location'][0:2]
                
            city_list.append(city)
            sale_Count=result['saleCount']
            sale_Count_list.append(sale_Count)

            
        #print(city_list)
        #print(sale_Count_list)

        city_saleCount_dict=self.stastic_saler_city(city_list,sale_Count_list)
        for key ,val in city_saleCount_dict.items():
            city_saleCount_dict_list.append((val,key))
            
            #print(key,val)
        for item in city_saleCount_dict_list:
            #print(type(i))
            #print(item[0],item[1])

            #只统计本月出售数大于5的城市
            if item[0]>=800:
                
                print(item[1],item[0])
                #print(type(item[1]))
                city_list_sum.append(item[1])#城市名
                city_sale_count_list.append(item[0])#数量
        #print(type(city_list[2]))
        
        self.show_city_data(city_list_sum,city_sale_count_list)
            
    def stastic_saler_city(self,city_list,sale_Count_list):
        city_dict={}
        k=0
        for i in city_list:
            
            if i in city_dict:
                
                city_dict[i]+=int(sale_Count_list[k])
            else:
                
                #city_dict[i]=int(sale_Count_list[k])
                #city_dict[i]=1
                city_dict[i]=int(sale_Count_list[k])
                #print(city_dict[i])
                
            k=k+1
        return city_dict





    #展示各城市总销量图

    def show_city_data(self,city_list,city_sale_count_list):
        #zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        #plt.xticks(b,city_list)
        a=plt.bar(range(len(city_sale_count_list)),city_sale_count_list,color='rgb',tick_label=city_list)
        self.autolabel(a)
       
        plt.xlabel(u"城市")  # 指定x轴描述信息
        plt.ylabel(self.key_word+"总销量图")  # 指定y轴描述信息
        plt.title(self.key_word+"各城市统计表")  # 指定图表描述信息
        #plt.savefig(self.key_word+"各城市统计表.png”)
        plt.xticks(rotation=20)
        plt.show()
        
    #------------------------------------------------------------------------商家描述词云图---------------------------------------------------------------
    def desc_word_cloud(self):
        results=self.products.find({'desc':{'$exists':True}})
        
        sava_file_path="F:\\Python_chenxu\\computer_prongram_contest\\data\\"
        sava_file_path=sava_file_path+self.MgodbName+r'.txt'
        #如果文件不存在则创建并保存内容
        if not os.access(sava_file_path, os.F_OK):
            
            print("Given file path is exist.")
         
            with open(sava_file_path,'a',encoding='utf-8') as f:
                
                for result in results:
                    
                    sale_desc_info=result['desc']#提取商家描述信息
                    
                    #对商家描述中字母和符号进行剔除
                    
                    bad1_str='&lt;span class=H&gt;'
                    bad2_str='&lt;/span&gt;'
                    bad3_str=self.key_word
                    bad4_str=self.key_word[0:2]
                    bad5_str='包邮'
                    
                    sale_desc_info=sale_desc_info.replace(bad1_str,'')
                    sale_desc_info=sale_desc_info.replace(bad2_str,'')
                    sale_desc_info=sale_desc_info.replace(bad3_str,'')
                    sale_desc_info=sale_desc_info.replace(bad4_str,'')
                    sale_desc_info=sale_desc_info.replace(bad5_str,'')
                    f.write(sale_desc_info)
                f.close()
        #文件存在读取信息     
        with open(sava_file_path,'r',encoding='utf-8') as f:
            
            file_content=f.read()
            result=jieba.cut(file_content)
            
            f1=open("F:\Python_chenxu\Word_Cloud\chineseStopWords.txt","r")
            stopwords={}.fromkeys(f1.read().split("\n"))
            f1.close()
            mytext_list=[]
            for seg in result:
                #print('seg',seg)
                if seg not in stopwords and seg!=" " and len(seg)!=1:
                    mytext_list.append(seg.replace(" ",""))
            cloud_text=",".join(mytext_list)
            #print(cloud_text)
            f.close()
        cloud_mask = np.array(Image.open("F:\Python_chenxu\Word_Cloud\yu_mao_qiu1.jpg"))
        wc = WordCloud(
        scale=1,#清晰程度
        mask=cloud_mask,
        #background_color="white", #背景颜色
        max_words=800, #显示最大词数
        font_path="F:\Python_chenxu\Word_Cloud\simfang.ttf",  #使用字体
        min_font_size=15,
        max_font_size=80, 
        width=500  #图幅宽度
        )
        wc2 =wc.generate(cloud_text)
        #wc.to_file("desc_word_cloud.gif")#保存文件
        plt.imshow(wc2)
        plt.title(self.key_word+"词云图",FontProperties=font_set)
        plt.axis("off")
        plt.show()
    #------------------------------------------------------------------------价格&与销售量图------------------------------------------------------------------
    def price_sale(self):
        results=self.products.find({'saleCount':{'$exists':True}}).sort('saleCount',pymongo.DESCENDING)#降序排序
        type_1_saleCount=[]
        type_1_price=[]
        type_2_saleCount=[]
        type_2_price=[]
        type_3_saleCount=[]
        type_3_price=[]
        i=200#挑出销售量排名前200个
        for result in results:
            comp=float(result['saleCount'])
            price=float(result['realPrice'])
            
            if (comp>3000):
                type_1_saleCount.append(comp)
                type_1_price.append(price)
                #print(type(result['saleCount']))

            elif (comp>500)&(comp<3000):
                type_2_saleCount.append(comp)
                type_2_price.append(price)
            elif (comp>20)&(comp<500):
                type_3_saleCount.append(comp)
                type_3_price.append(price)
            elif i==0:
                #print(i)
                break
            else:
                continue
            #print(i)
            i -=1

                
        #print(type_1_saleCount,':',type_1_price)
        zhfont = font_set
     
        plt.figure(figsize=(8, 5), dpi=80)
        axes = plt.subplot(111)
        type1 = axes.scatter(type_1_price, type_1_saleCount,s=20, c='red')
        type2=axes.scatter(type_2_price, type_2_saleCount, s=40, c='green')
        type3=axes.scatter(type_3_price, type_3_saleCount, s=50, c='blue')

        
        #axes.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')  
        #axes.set_xlim([0, 600])
        #axes.set_xticks([0,10,20,40,50,100 ,150,200,300,3000])   
        tick_spacing =40
        #plt.xlim(0, 200)

        plt.title(self.key_word+'售价与月销售总量散点图',fontproperties=zhfont)
        plt.xlabel('售价', fontproperties=zhfont)
        plt.ylabel('月销售总量',  fontproperties=zhfont)
        axes.legend((type1, type2, type3),('5000以上', '500-5000', '500以下'),loc=1, prop=zhfont)

        axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
       
        #plt.plot(type_3_price, type_3_saleCount, 'ro')
        plt.xticks(rotation=35)
        plt.show()
            
            
    #运行程序
    def run(self,i):
        #1表示爬取数据和删除重复数据
        if (i==1):
            
            self.requests_one_page()
            self.delet_repeat_items()
        #2表示显示每个省总店铺数量
        elif (i==2):  
            
            self.data_anlysis()
      
        #3每个城市总销量图
        
        elif(i==3):
            self.city_saleCount()
       
        #4商家描述词云图
        elif (i==4):
            self.desc_word_cloud()
        #5表示销售量与价格走向图
        elif (i==5):
            self.price_sale()
        
        else:
            print("输入不合法")
            


if __name__ == '__main__':
    a=CrawlProduct('西瓜','apple')
    a.run(2)




    
