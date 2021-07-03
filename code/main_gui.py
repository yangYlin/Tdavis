'''
本作品由西南大学计信院杨远林所编写
版权归杨远林所有，违者必追究法律责任
最终解释权由杨远林决定
''''




import tkinter as tk  # 使用Tkinter前需要先导入
import PIL
from PIL import Image, ImageTk #加载jpg格式或者png格式图片
import sys

import tkinter.messagebox
 
sys.path.append(r"F:\Python_chenxu\computer_prongram_contest\class")
from catch_data_show import *

sys.path.append(r"F:\Python_chenxu\computer_prongram_contest\class\proxy")
from RdisClient import *
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('淘宝商品数据可视化系统')
        self.window.geometry('800x600')  # 这里的乘是小x
        self.l = tk.Label(self.window, text='      ', bg='green')
        self.counter = 0
        self.menubar = tk.Menu(self.window)
    def Labe(self):
        self.l = tk.Label(self.window, text='      ', bg='green')
        self.l.pack()
    def do_job(self):
        self.counter
        self.l.config(text='do '+ str(self.counter))
        self.counter += self.l
    def show_photo(self):
        file='F:\Python_chenxu\GUI_data_show\data\spider2.png'

        img_open = Image.open(file)
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.window, image = img_png)
        label_img.pack(expland=1)
        
    def  do_pronvince(self):
        a=CrawlProduct()
        a.run(2)
    def  do_city(self):
        a=CrawlProduct()
        a.run(3)
    def  do_word_cloud(self):
        a=CrawlProduct()
        a.run(4)
    def  do_sale_price(self):
        a=CrawlProduct()
        a.run(5)
    def  lanqiu_do_pronvince(self):
        a=CrawlProduct('篮球','lanqiu')
        #a.run(1)
        a.run(2)
    def  lanqiu_do_city(self):
        a=CrawlProduct('篮球','lanqiu')
        a.run(3)
    def  lanqiu_do_word_cloud(self):
        a=CrawlProduct('篮球','lanqiu')
        a.run(4)
    def  lanqiu_do_sale_price(self):
        a=CrawlProduct('篮球','lanqiu')
        a.run(5)
        
    def  zuqiu_do_pronvince(self):
        a=CrawlProduct('足球','zuqiu')
        #a.run(1)
        a.run(2)
    def  zuqiu_do_city(self):
        a=CrawlProduct('足球','zuqiu')
        a.run(3)
    def  zuqiu_do_word_cloud(self):
        a=CrawlProduct('足球','zuqiu')
        a.run(4)
    def  zuqiu_do_sale_price(self):
        a=CrawlProduct('足球','zuqiu')
        a.run(5)

    def  bingbangqiu_zuqiu_do_pronvince(self):
        a=CrawlProduct('兵乓球拍','bingbangqiu')
        #a.run(1)
        a.run(2)
    def  bingbangqiu_do_city(self):
        a=CrawlProduct('兵乓球拍','bingbangqiu')
        a.run(3)
    def  bingbangqiu_do_word_cloud(self):
        a=CrawlProduct('兵乓球拍','bingbangqiu')
        a.run(4)
    def  bingbangqiu_do_sale_price(self):
        a=CrawlProduct('兵乓球拍','bingbangqiu')
        a.run(5)
        
   #-------------------------------------------------------------------------------------------------------------------------------------------------热门推荐模块-------------------------------------------------
    def   ren_men_tui_quan(self):
       
        ren_men_tui_quan = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='热门推荐  ', menu=ren_men_tui_quan)
        
        yumaoqiu = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='羽毛球拍', menu=yumaoqiu, underline=0) # 给放入的菜单submenu命名为Import
        yumaoqiu.add_command(label='省分布图', command=self.do_pronvince)
        yumaoqiu.add_command(label='城市分布图', command=self.do_city)
        yumaoqiu.add_command(label='词云图', command=self.do_word_cloud)
        yumaoqiu.add_command(label='销量售价图', command=self.do_sale_price)

        ren_men_tui_quan.add_separator()    # 添加一条分隔线
        
        weiyi = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='卫衣', menu=weiyi, underline=0) # 给放入的菜单submenu命名为Import
        weiyi.add_command(label='省分布图', command=self.weiyi_zuqiu_do_pronvince)
        weiyi.add_command(label='城市分布图', command=self.weiyi_do_city)
        weiyi.add_command(label='词云图', command=self.weiyi_do_word_cloud)
        weiyi.add_command(label='销量售价图', command=self.weiyi_do_sale_price)

        
        cunyi = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='衬衣', menu=cunyi, underline=0) # 给放入的菜单submenu命名为Import
        cunyi.add_command(label='省分布图', command=self.cunyi_zuqiu_do_pronvince)
        cunyi.add_command(label='城市分布图', command=self.cunyi_do_city)
        cunyi.add_command(label='词云图', command=self.cunyi_do_word_cloud)
        cunyi.add_command(label='销量售价图', command=self.cunyi_do_sale_price)

        ren_men_tui_quan.add_separator()    # 添加一条分隔线

        xiyiji = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='洗衣机', menu=xiyiji, underline=0) 
        xiyiji.add_command(label='省分布图', command=self.xiyiji_zuqiu_do_pronvince)
        xiyiji.add_command(label='城市分布图', command=self.xiyiji_do_city)
        xiyiji.add_command(label='词云图', command=self.xiyiji_do_word_cloud)
        xiyiji.add_command(label='销量售价图', command=self.xiyiji_do_sale_price)
        
        bijiben = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='笔记本电脑', menu=bijiben, underline=0)
        bijiben.add_command(label='省分布图', command=self.bijiben_zuqiu_do_pronvince)
        bijiben.add_command(label='城市分布图', command=self.bijiben_do_city)
        bijiben.add_command(label='词云图', command=self.bijiben_do_word_cloud)
        bijiben.add_command(label='销量售价图', command=self.bijiben_do_sale_price)

        ren_men_tui_quan.add_separator()    # 添加一条分隔线

        yintao = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='樱桃', menu=yintao, underline=0) 
        yintao.add_command(label='省分布图', command=self.yintao_zuqiu_do_pronvince)
        yintao.add_command(label='城市分布图', command=self.yintao_do_city)
        yintao.add_command(label='词云图', command=self.yintao_do_word_cloud)
        yintao.add_command(label='销量售价图', command=self.yintao_do_sale_price)


        chaye = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='茶叶', menu=chaye, underline=0) 
        chaye.add_command(label='省分布图', command=self.chaye_zuqiu_do_pronvince)
        chaye.add_command(label='城市分布图', command=self.chaye_do_city)
        chaye.add_command(label='词云图', command=self.chaye_do_word_cloud)
        chaye.add_command(label='销量售价图', command=self.chaye_do_sale_price)
        
        ren_men_tui_quan.add_separator()    # 添加一条分隔线

        canjinzi = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='餐巾纸', menu=canjinzi, underline=0) 
        canjinzi.add_command(label='省分布图', command=self.canjinzi_do_pronvince)
        canjinzi.add_command(label='城市分布图', command=self.canjinzi_do_city)
        canjinzi.add_command(label='词云图', command=self.canjinzi_do_word_cloud)
        canjinzi.add_command(label='销量售价图', command=self.canjinzi_do_sale_price)
        
        yahua = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='牙刷', menu=yahua, underline=0) 
        yahua.add_command(label='省分布图', command=self.yahua_do_pronvince)
        yahua.add_command(label='城市分布图', command=self.yahua_do_city)
        yahua.add_command(label='词云图', command=self.yahua_do_word_cloud)
        yahua.add_command(label='销量售价图', command=self.yahua_do_sale_price)

        ren_men_tui_quan.add_separator()    # 添加一条分隔线
        mudan = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='牡丹', menu=mudan, underline=0) 
        mudan.add_command(label='省分布图', command=self.qianbao_do_pronvince)
        mudan.add_command(label='城市分布图', command=self.qianbao_do_city)
        mudan.add_command(label='词云图', command=self.qianbao_do_word_cloud)
        mudan.add_command(label='销量售价图', command=self.qianbao_do_sale_price)

        lanhua = tk.Menu(ren_men_tui_quan)
        ren_men_tui_quan.add_cascade(label='兰花', menu=lanhua,font=('Arial', 20), underline=0) 
        lanhua.add_command(label='省分布图', command=self.qianbao_do_pronvince)
        lanhua.add_command(label='城市分布图', command=self.qianbao_do_city)
        lanhua.add_command(label='词云图', command=self.qianbao_do_word_cloud)
        lanhua.add_command(label='销量售价图', command=self.qianbao_do_sale_price)
                                                 


    #--------------------------------------------------------------------------------------------------------------------------体育模块--------------------------------------------------------------------------------------------------------------------------------------
    def   PF(self):
        # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
        PeMenu = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='体育  ', menu=PeMenu)
         

        #PeMenu.add_command(label='篮球', command=do_job)
        lanqiu = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='篮球', menu=lanqiu, underline=0) # 给放入的菜单submenu命名为Import
        lanqiu.add_command(label='省分布图', command=self.lanqiu_do_pronvince)
        lanqiu.add_command(label='城市分布图', command=self.lanqiu_do_city)
        lanqiu.add_command(label='词云图', command=self.lanqiu_do_word_cloud)
        lanqiu.add_command(label='销量售价图', command=self.lanqiu_do_sale_price)
            

        
        zuqiu = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='足球', menu=zuqiu, underline=0) # 给放入的菜单submenu命名为Import
        zuqiu.add_command(label='省分布图', command=self.zuqiu_do_pronvince)
        zuqiu.add_command(label='城市分布图', command=self.zuqiu_do_city)
        zuqiu.add_command(label='词云图', command=self.zuqiu_do_word_cloud)
        zuqiu.add_command(label='销量售价图', command=self.zuqiu_do_sale_price)


        yumaoqiu = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='羽毛球拍', menu=yumaoqiu, underline=0) # 给放入的菜单submenu命名为Import
        yumaoqiu.add_command(label='省分布图', command=self.do_pronvince)
        yumaoqiu.add_command(label='城市分布图', command=self.do_city)
        yumaoqiu.add_command(label='词云图', command=self.do_word_cloud)
        yumaoqiu.add_command(label='销量售价图', command=self.do_sale_price)



        bingbangqiu = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='兵乓球拍', menu=bingbangqiu, underline=0) # 给放入的菜单submenu命名为Import
        bingbangqiu.add_command(label='省分布图', command=self.bingbangqiu_zuqiu_do_pronvince)
        bingbangqiu.add_command(label='城市分布图', command=self.bingbangqiu_do_city)
        bingbangqiu.add_command(label='词云图', command=self.bingbangqiu_do_word_cloud)
        bingbangqiu.add_command(label='销量售价图', command=self.bingbangqiu_do_sale_price)
    def  weiyi_zuqiu_do_pronvince(self):
        a=CrawlProduct('卫衣','weiyi')
        #a.run(1)
        a.run(2)
    def  weiyi_do_city(self):
        a=CrawlProduct('卫衣','weiyi')
        a.run(3)
    def  weiyi_do_word_cloud(self):
        a=CrawlProduct('卫衣','weiyi')
        a.run(4)
    def  weiyi_do_sale_price(self):
        a=CrawlProduct('卫衣','weiyi')
        a.run(5)
        
    def  waiyi_zuqiu_do_pronvince(self):
        a=CrawlProduct('外衣','waiyi')
        #a.run(1)
        a.run(2)
    def  waiyi_do_city(self):
        a=CrawlProduct('外衣','waiyi')
        a.run(3)
    def  waiyi_do_word_cloud(self):
        a=CrawlProduct('衬衣','waiyi')
        a.run(4)
    def  waiyi_do_sale_price(self):
        a=CrawlProduct('外衣','waiyi')
        a.run(5)
        
    def  cunyi_zuqiu_do_pronvince(self):
        a=CrawlProduct('衬衣','cunyi')
        #a.run(1)
        a.run(2)
    def  cunyi_do_city(self):
        a=CrawlProduct('衬衣','cunyi')
        a.run(3)
    def  cunyi_do_word_cloud(self):
        a=CrawlProduct('衬衣','cunyi')
        a.run(4)
    def  cunyi_do_sale_price(self):
        a=CrawlProduct('衬衣','cunyi')
        a.run(5)

        
    def  duanxiu_zuqiu_do_pronvince(self):
        a=CrawlProduct('短袖','duanxiu')
        #a.run(1)
        a.run(2)
    def  duanxiu_do_city(self):
        a=CrawlProduct('短袖','duanxiu')
        a.run(3)
    def duanxiu_do_word_cloud(self):
        a=CrawlProduct('短袖','duanxiu')
        a.run(4)
    def  duanxiu_do_sale_price(self):
        a=CrawlProduct('短袖','duanxiu')
        a.run(5)
        
    def  pixie_zuqiu_do_pronvince(self):
        a=CrawlProduct('皮鞋','pixie')
        #a.run(1)
        a.run(2)
    def  pixie_do_city(self):
        a=CrawlProduct('皮鞋','pixie')
        a.run(3)
    def pixie_do_word_cloud(self):
        a=CrawlProduct('皮鞋','pixie')
        a.run(4)
    def  pixie_do_sale_price(self):
        a=CrawlProduct('皮鞋','pixie')
        a.run(5)

        
    def  fanbuxie_zuqiu_do_pronvince(self):
        a=CrawlProduct('帆布鞋','fanbuxie')
        #a.run(1)
        a.run(2)
    def  fanbuxie_do_city(self):
        a=CrawlProduct('帆布鞋','fanbuxie')
        a.run(3)
    def fanbuxie_do_word_cloud(self):
        a=CrawlProduct('帆布鞋','fanbuxie')
        a.run(4)
    def  fanbuxie_do_sale_price(self):
        a=CrawlProduct('帆布鞋','fanbuxie')
        a.run(5)

    def  changku_zuqiu_do_pronvince(self):
        a=CrawlProduct('长裤','changku')
        #a.run(1)
        a.run(2)
    def  changku_do_city(self):
        a=CrawlProduct('长裤','changku')
        a.run(3)
    def changku_do_word_cloud(self):
        a=CrawlProduct('长裤','changku')
        a.run(4)
    def  changku_do_sale_price(self):
        a=CrawlProduct('长裤','changku')
        a.run(5)


        

    #-------------------------------------------------------------------------------------------------------------------------服装模块-------------------------------------------------
    def   fu_zhuang(self):
        # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
        PeMenu = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='服装  ', menu=PeMenu)
         

        #PeMenu.add_command(label='篮球', command=do_job)
        weiyi = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='卫衣', menu=weiyi, underline=0) # 给放入的菜单submenu命名为Import
        weiyi.add_command(label='省分布图', command=self.weiyi_zuqiu_do_pronvince)
        weiyi.add_command(label='城市分布图', command=self.weiyi_do_city)
        weiyi.add_command(label='词云图', command=self.weiyi_do_word_cloud)
        weiyi.add_command(label='销量售价图', command=self.weiyi_do_sale_price)

        
        waiyi = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='外衣', menu=waiyi, underline=0) # 给放入的菜单submenu命名为Import
        waiyi.add_command(label='省分布图', command=self.waiyi_zuqiu_do_pronvince)
        waiyi.add_command(label='城市分布图', command=self.waiyi_do_city)
        waiyi.add_command(label='词云图', command=self.waiyi_do_word_cloud)
        waiyi.add_command(label='销量售价图', command=self.waiyi_do_sale_price)


        cunyi = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='衬衣', menu=cunyi, underline=0) # 给放入的菜单submenu命名为Import
        cunyi.add_command(label='省分布图', command=self.cunyi_zuqiu_do_pronvince)
        cunyi.add_command(label='城市分布图', command=self.cunyi_do_city)
        cunyi.add_command(label='词云图', command=self.cunyi_do_word_cloud)
        cunyi.add_command(label='销量售价图', command=self.cunyi_do_sale_price)



        duanxiu = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='短袖', menu=duanxiu, underline=0) # 给放入的菜单submenu命名为Import
        duanxiu.add_command(label='省分布图', command=self.duanxiu_zuqiu_do_pronvince)
        duanxiu.add_command(label='城市分布图', command=self.duanxiu_do_city)
        duanxiu.add_command(label='词云图', command=self.duanxiu_do_word_cloud)
        duanxiu.add_command(label='销量售价图', command=self.duanxiu_do_sale_price)
        
        pixie = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='皮鞋', menu=pixie, underline=0) # 给放入的菜单submenu命名为Import
        pixie.add_command(label='省分布图', command=self.pixie_zuqiu_do_pronvince)
        pixie.add_command(label='城市分布图', command=self.pixie_do_city)
        pixie.add_command(label='词云图', command=self.pixie_do_word_cloud)
        pixie.add_command(label='销量售价图', command=self.pixie_do_sale_price)


        fanbuxie = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='帆布鞋', menu=fanbuxie, underline=0) # 给放入的菜单submenu命名为Import
        fanbuxie.add_command(label='省分布图', command=self.fanbuxie_zuqiu_do_pronvince)
        fanbuxie.add_command(label='城市分布图', command=self.fanbuxie_do_city)
        fanbuxie.add_command(label='词云图', command=self.fanbuxie_do_word_cloud)
        fanbuxie.add_command(label='销量售价图', command=self.fanbuxie_do_sale_price)
        
        changku = tk.Menu(PeMenu)
        PeMenu.add_cascade(label='长裤', menu=changku, underline=0) # 给放入的菜单submenu命名为Import
        changku.add_command(label='省分布图', command=self.changku_zuqiu_do_pronvince)
        changku.add_command(label='城市分布图', command=self.changku_do_city)
        changku.add_command(label='词云图', command=self.changku_do_word_cloud)
        changku.add_command(label='销量售价图', command=self.changku_do_sale_price)


        
    def  congdianbao_zuqiu_do_pronvince(self):
        a=CrawlProduct('充电宝','congdianbao')
        #a.run(1)
        a.run(2)
    def  congdianbao_do_city(self):
        a=CrawlProduct('充电宝','congdianbao')
        a.run(3)
    def congdianbao_do_word_cloud(self):
        a=CrawlProduct('充电宝','congdianbao')
        a.run(4)
    def  congdianbao_do_sale_price(self):
        a=CrawlProduct('充电宝','congdianbao')
        a.run(5)


    def  zhaoxiangj_zuqiu_do_pronvince(self):
        a=CrawlProduct('照相机','zhaoxiangj')
        #a.run(1)
        a.run(2)
    def  zhaoxiangj_do_city(self):
        a=CrawlProduct('照相机','zhaoxiangj')
        a.run(3)
    def zhaoxiangj_do_word_cloud(self):
        a=CrawlProduct('照相机','zhaoxiangj')
        a.run(4)
    def  zhaoxiangj_do_sale_price(self):
        a=CrawlProduct('照相机','zhaoxiangj')
        a.run(5)

        
    def  bingxiang_zuqiu_do_pronvince(self):
        a=CrawlProduct('冰箱','bingxiang')
        #a.run(1)
        a.run(2)
    def  bingxiang_do_city(self):
        a=CrawlProduct('冰箱','bingxiang')
        a.run(3)
    def bingxiang_do_word_cloud(self):
        a=CrawlProduct('冰箱','bingxiang')
        a.run(4)
    def  bingxiang_do_sale_price(self):
        a=CrawlProduct('冰箱','bingxiang')
        a.run(5)


        
    def  xiyiji_zuqiu_do_pronvince(self):
        a=CrawlProduct('洗衣机','xiyiji')
        #a.run(1)
        a.run(2)
    def  xiyiji_do_city(self):
        a=CrawlProduct('洗衣机','xiyiji')
        a.run(3)
    def xiyiji_do_word_cloud(self):
        a=CrawlProduct('洗衣机','xiyiji')
        a.run(4)
    def  xiyiji_do_sale_price(self):
        a=CrawlProduct('洗衣机','xiyiji')
        a.run(5)


        
    def  bijiben_zuqiu_do_pronvince(self):
        a=CrawlProduct('笔记本电脑','bijiben')
        #a.run(1)
        a.run(2)
    def bijiben_do_city(self):
        a=CrawlProduct('笔记本电脑','bijiben')
        a.run(3)
    def bijiben_do_word_cloud(self):
        a=CrawlProduct('笔记本电脑','bijiben')
        a.run(4)
    def  bijiben_do_sale_price(self):
        a=CrawlProduct('笔记本电脑','bijiben')
        a.run(5)

        
    def  jianpan_zuqiu_do_pronvince(self):
        a=CrawlProduct('键盘','jianpan')
        #a.run(1)
        a.run(2)
    def jianpan_do_city(self):
        a=CrawlProduct('键盘','jianpan')
        a.run(3)
    def jianpan_do_word_cloud(self):
        a=CrawlProduct('键盘','jianpan')
        a.run(4)
    def  jianpan_do_sale_price(self):
        a=CrawlProduct('键盘','jianpan')
        a.run(5)


        
    def  dianfanguo_zuqiu_do_pronvince(self):
        a=CrawlProduct('电饭锅','dianfanguo')
        #a.run(1)
        a.run(2)
    def dianfanguo_do_city(self):
        a=CrawlProduct('电饭锅','dianfanguo')
        a.run(3)
    def dianfanguo_do_word_cloud(self):
        a=CrawlProduct('电饭锅','dianfanguo')
        a.run(4)
    def  dianfanguo_do_sale_price(self):
        a=CrawlProduct('电饭锅','dianfanguo')
        a.run(5)


        
    def  lanyaerji_zuqiu_do_pronvince(self):
        a=CrawlProduct('蓝牙耳机','lanyaerji')
        #a.run(1)
        a.run(2)
    def lanyaerji_do_city(self):
        a=CrawlProduct('蓝牙耳机','lanyaerji')
        a.run(3)
    def lanyaerji_do_word_cloud(self):
        a=CrawlProduct('蓝牙耳机','lanyaerji')
        a.run(4)
    def  lanyaerji_do_sale_price(self):
        a=CrawlProduct('蓝牙耳机','lanyaerji')
        a.run(5)




    #-------------------------------------------------------------------------------------------------------------------------------------------------数码模块-------------------------------------------------
    def   shu_ma(self):
        
        shu_ma = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='数码  ', menu=shu_ma)
         

       
        congdianbao = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='充电宝', menu=congdianbao, underline=0) 
        congdianbao.add_command(label='省分布图', command=self.congdianbao_zuqiu_do_pronvince)
        congdianbao.add_command(label='城市分布图', command=self.congdianbao_do_city)
        congdianbao.add_command(label='词云图', command=self.congdianbao_do_word_cloud)
        congdianbao.add_command(label='销量售价图', command=self.congdianbao_do_sale_price)

        
        zhaoxiangj = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='照相机', menu=zhaoxiangj, underline=0) 
        zhaoxiangj.add_command(label='省分布图', command=self.zhaoxiangj_zuqiu_do_pronvince)
        zhaoxiangj.add_command(label='城市分布图', command=self.zhaoxiangj_do_city)
        zhaoxiangj.add_command(label='词云图', command=self.zhaoxiangj_do_word_cloud)
        zhaoxiangj.add_command(label='销量售价图', command=self.zhaoxiangj_do_sale_price)


        bingxiang = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='冰箱', menu=bingxiang, underline=0) 
        bingxiang.add_command(label='省分布图', command=self.bingxiang_zuqiu_do_pronvince)
        bingxiang.add_command(label='城市分布图', command=self.bingxiang_do_city)
        bingxiang.add_command(label='词云图', command=self.bingxiang_do_word_cloud)
        bingxiang.add_command(label='销量售价图', command=self.bingxiang_do_sale_price)



        xiyiji = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='洗衣机', menu=xiyiji, underline=0) 
        xiyiji.add_command(label='省分布图', command=self.xiyiji_zuqiu_do_pronvince)
        xiyiji.add_command(label='城市分布图', command=self.xiyiji_do_city)
        xiyiji.add_command(label='词云图', command=self.xiyiji_do_word_cloud)
        xiyiji.add_command(label='销量售价图', command=self.xiyiji_do_sale_price)
        
        bijiben = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='笔记本电脑', menu=bijiben, underline=0)
        bijiben.add_command(label='省分布图', command=self.bijiben_zuqiu_do_pronvince)
        bijiben.add_command(label='城市分布图', command=self.bijiben_do_city)
        bijiben.add_command(label='词云图', command=self.bijiben_do_word_cloud)
        bijiben.add_command(label='销量售价图', command=self.bijiben_do_sale_price)


        jianpan = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='键盘', menu=jianpan, underline=0) 
        jianpan.add_command(label='省分布图', command=self.jianpan_zuqiu_do_pronvince)
        jianpan.add_command(label='城市分布图', command=self.jianpan_do_city)
        jianpan.add_command(label='词云图', command=self.jianpan_do_word_cloud)
        jianpan.add_command(label='销量售价图', command=self.jianpan_do_sale_price)

    
        dianfanguo = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='电饭锅', menu=dianfanguo, underline=0) 
        dianfanguo.add_command(label='省分布图', command=self.dianfanguo_zuqiu_do_pronvince)
        dianfanguo.add_command(label='城市分布图', command=self.dianfanguo_do_city)
        dianfanguo.add_command(label='词云图', command=self.dianfanguo_do_word_cloud)
        dianfanguo.add_command(label='销量售价图', command=self.dianfanguo_do_sale_price)


        lanyaerji = tk.Menu(shu_ma)
        shu_ma.add_cascade(label='蓝牙耳机', menu=lanyaerji, underline=0)
        lanyaerji.add_command(label='省分布图', command=self.lanyaerji_zuqiu_do_pronvince)
        lanyaerji.add_command(label='城市分布图', command=self.lanyaerji_do_city)
        lanyaerji.add_command(label='词云图', command=self.lanyaerji_do_word_cloud)
        lanyaerji.add_command(label='销量售价图', command=self.lanyaerji_do_sale_price)


    def  mianbao_do_pronvince(self):
        a=CrawlProduct('面包','mianbao')
        #a.run(1)
        a.run(2)
    def mianbao_do_city(self):
        a=CrawlProduct('面包','mianbao')
        a.run(3)
    def mianbao_do_word_cloud(self):
        a=CrawlProduct('面包','mianbao')
        a.run(4)
    def  mianbao_do_sale_price(self):
        a=CrawlProduct('面包','mianbao')
        a.run(5)




    def  yintao_zuqiu_do_pronvince(self):
        a=CrawlProduct('樱桃','yintao')
        #a.run(1)
        a.run(2)
    def yintao_do_city(self):
        a=CrawlProduct('樱桃','yintao')
        a.run(3)
    def yintao_do_word_cloud(self):
        a=CrawlProduct('樱桃','yintao')
        a.run(4)
    def yintao_do_sale_price(self):
        a=CrawlProduct('樱桃','yintao')
        a.run(5)

    def  chaye_zuqiu_do_pronvince(self):
        a=CrawlProduct('茶叶','chaye')
        #a.run(1)
        a.run(2)
    def chaye_do_city(self):
        a=CrawlProduct('茶叶','chaye')
        a.run(3)
    def chaye_do_word_cloud(self):
        a=CrawlProduct('茶叶','chaye')
        a.run(4)
    def chaye_do_sale_price(self):
        a=CrawlProduct('茶叶','chaye')
        a.run(5)



    def  suanniunai_zuqiu_do_pronvince(self):
        a=CrawlProduct('酸牛奶','suanniunai')
        #a.run(1)
        a.run(2)
    def suanniunai_do_city(self):
        a=CrawlProduct('酸牛奶','suanniunai')
        a.run(3)
    def suanniunai_do_word_cloud(self):
        a=CrawlProduct('酸牛奶','suanniunai')
        a.run(4)
    def suanniunai_do_sale_price(self):
        a=CrawlProduct('酸牛奶','suanniunai')
        a.run(5)


    def  dangao_zuqiu_do_pronvince(self):
        a=CrawlProduct('蛋糕','dangao')
        #a.run(1)
        a.run(2)
    def dangao_do_city(self):
        a=CrawlProduct('蛋糕','dangao')
        a.run(3)
    def dangao_do_word_cloud(self):
        a=CrawlProduct('蛋糕','dangao')
        a.run(4)
    def dangao_do_sale_price(self):
        a=CrawlProduct('蛋糕','dangao')
        a.run(5)


    def  xiaolongxia_zuqiu_do_pronvince(self):
        a=CrawlProduct('小龙虾','xiaolongxia')
        #a.run(1)
        a.run(2)
    def xiaolongxia_do_city(self):
        a=CrawlProduct('小龙虾','xiaolongxia')
        a.run(3)
    def xiaolongxia_do_word_cloud(self):
        a=CrawlProduct('小龙虾','xiaolongxia')
        a.run(4)
    def xiaolongxia_do_sale_price(self):
        a=CrawlProduct('小龙虾','xiaolongxia')
        a.run(5)



    #-------------------------------------------------------------------------------------------------------------------------------------------------美食模块-------------------------------------------------
    def   mei_si(self):
        
        mei_si = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='美食  ', menu=mei_si)
         

        
        mianbao = tk.Menu(mei_si)
        mei_si.add_cascade(label='面包', menu=mianbao, underline=0) 
        mianbao.add_command(label='省分布图', command=self.mianbao_do_pronvince)
        mianbao.add_command(label='城市分布图', command=self.mianbao_do_city)
        mianbao.add_command(label='词云图', command=self.mianbao_do_word_cloud)
        mianbao.add_command(label='销量售价图', command=self.mianbao_do_sale_price)

        
        yintao = tk.Menu(mei_si)
        mei_si.add_cascade(label='樱桃', menu=yintao, underline=0) 
        yintao.add_command(label='省分布图', command=self.yintao_zuqiu_do_pronvince)
        yintao.add_command(label='城市分布图', command=self.yintao_do_city)
        yintao.add_command(label='词云图', command=self.yintao_do_word_cloud)
        yintao.add_command(label='销量售价图', command=self.yintao_do_sale_price)


        chaye = tk.Menu(mei_si)
        mei_si.add_cascade(label='茶叶', menu=chaye, underline=0) 
        chaye.add_command(label='省分布图', command=self.chaye_zuqiu_do_pronvince)
        chaye.add_command(label='城市分布图', command=self.chaye_do_city)
        chaye.add_command(label='词云图', command=self.chaye_do_word_cloud)
        chaye.add_command(label='销量售价图', command=self.chaye_do_sale_price)



        suanniunai = tk.Menu(mei_si)
        mei_si.add_cascade(label='酸牛奶', menu=suanniunai, underline=0) 
        suanniunai.add_command(label='省分布图', command=self.suanniunai_zuqiu_do_pronvince)
        suanniunai.add_command(label='城市分布图', command=self.suanniunai_do_city)
        suanniunai.add_command(label='词云图', command=self.suanniunai_do_word_cloud)
        suanniunai.add_command(label='销量售价图', command=self.suanniunai_do_sale_price)

        
        dangao = tk.Menu(mei_si)
        mei_si.add_cascade(label='蛋糕', menu=dangao, underline=0) 
        dangao.add_command(label='省分布图', command=self.dangao_zuqiu_do_pronvince)
        dangao.add_command(label='城市分布图', command=self.dangao_do_city)
        dangao.add_command(label='词云图', command=self.dangao_do_word_cloud)
        dangao.add_command(label='销量售价图', command=self.dangao_do_sale_price)


        xiaolongxia = tk.Menu(mei_si)
        mei_si.add_cascade(label='小龙虾', menu=xiaolongxia, underline=0) 
        xiaolongxia.add_command(label='省分布图', command=self.xiaolongxia_zuqiu_do_pronvince)
        xiaolongxia.add_command(label='城市分布图', command=self.xiaolongxia_do_city)
        xiaolongxia.add_command(label='词云图', command=self.xiaolongxia_do_word_cloud)
        xiaolongxia.add_command(label='销量售价图', command=self.xiaolongxia_do_sale_price)



    def  chuanlian_zuqiu_do_pronvince(self):
        a=CrawlProduct('窗帘','chuanlian')
        #a.run(1)
        a.run(2)
    def chuanlian_do_city(self):
        a=CrawlProduct('窗帘','chuanlian')
        a.run(3)
    def chuanlian_do_word_cloud(self):
        a=CrawlProduct('窗帘','chuanlian')
        a.run(4)
    def chuanlian_do_sale_price(self):
        a=CrawlProduct('窗帘','chuanlian')
        a.run(5)

    def shafa_do_pronvince(self):
        
        a=CrawlProduct('沙发','shafa')
        #a.run(1)
        a.run(2)
    def shafa_do_city(self):
        a=CrawlProduct('沙发','shafa')
        a.run(3)
    def shafa_do_word_cloud(self):
        a=CrawlProduct('沙发','shafa')
        a.run(4)
    def shafa_do_sale_price(self):
        a=CrawlProduct('沙发','shafa')
        a.run(5)
  
    def  baowenbei_zuqiu_do_pronvince(self):
        a=CrawlProduct('保温杯','baowenbei')
        #a.run(1)
        a.run(2)
    def baowenbei_do_city(self):
        a=CrawlProduct('保温杯','baowenbei')
        a.run(3)
    def baowenbei_do_word_cloud(self):
        a=CrawlProduct('保温杯','baowenbei')
        a.run(4)
    def baowenbei_do_sale_price(self):
        a=CrawlProduct('保温杯','baowenbei')
        a.run(5)

    
    def  yijia_zuqiu_do_pronvince(self):
        a=CrawlProduct('衣架','yijia')
        #a.run(1)
        a.run(2)
    def yijia_do_city(self):
        a=CrawlProduct('衣架','yijia')
        a.run(3)
    def yijia_do_word_cloud(self):
        a=CrawlProduct('衣架','yijia')
        a.run(4)
    def yijia_do_sale_price(self):
        a=CrawlProduct('衣架','yijia')
        a.run(5)


    def xiejia_do_pronvince(self):
        a=CrawlProduct('鞋架','xiejia')
        #a.run(1)
        a.run(2)
    def xiejia_do_city(self):
        a=CrawlProduct('鞋架','xiejia')
        a.run(3)
    def xiejia_do_word_cloud(self):
        a=CrawlProduct('鞋架','xiejia')
        a.run(4)
    def xiejia_do_sale_price(self):
        a=CrawlProduct('鞋架','xiejia')
        a.run(5)

    def canjinzi_do_pronvince(self):
        a=CrawlProduct('餐巾纸','canjinzi')
        #a.run(1)
        a.run(2)
    def canjinzi_do_city(self):
        a=CrawlProduct('餐巾纸','canjinzi')
        a.run(3)
    def canjinzi_do_word_cloud(self):
        a=CrawlProduct('餐巾纸','canjinzi')
        a.run(4)
    def canjinzi_do_sale_price(self):
        a=CrawlProduct('餐巾纸','canjinzi')
        a.run(5)        


    def yahua_do_pronvince(self):
        a=CrawlProduct('牙刷','yahua')
        #a.run(1)
        a.run(2)
    def yahua_do_city(self):
        a=CrawlProduct('牙刷','yahua')
        a.run(3)
    def yahua_do_word_cloud(self):
        a=CrawlProduct('牙刷','yahua')
        a.run(4)
    def yahua_do_sale_price(self):
        a=CrawlProduct('牙刷','yahua')
        a.run(5)        

    def yizi_do_pronvince(self):
        a=CrawlProduct('椅子','yizi')
        #a.run(1)
        a.run(2)
    def yizi_do_city(self):
        a=CrawlProduct('椅子','yizi')
        a.run(3)
    def yizi_do_word_cloud(self):
        a=CrawlProduct('椅子','yizi')
        a.run(4)
    def yizi_do_sale_price(self):
        a=CrawlProduct('椅子','yizi')
        a.run(5)

   '''
本作品由西南大学计信院杨远林所编写
版权归杨远林所有，违者必追究法律责任
最终解释权由杨远林决定
''''
#-------------------------------------------------------------------------------------------------------------------------------------------------家居模块-------------------------------------------------
    def   jia_ju(self):
       
        jia_ju = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='家居  ', menu=jia_ju)
         

       
        chuanlian = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='窗帘', menu=chuanlian, underline=0) 
        chuanlian.add_command(label='省分布图', command=self.chuanlian_zuqiu_do_pronvince)
        chuanlian.add_command(label='城市分布图', command=self.chuanlian_do_city)
        chuanlian.add_command(label='词云图', command=self.chuanlian_do_word_cloud)
        chuanlian.add_command(label='销量售价图', command=self.chuanlian_do_sale_price)

        
        shafa = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='沙发', menu=shafa, underline=0)
        shafa.add_command(label='省分布图', command=self.shafa_do_pronvince)
        shafa.add_command(label='城市分布图', command=self.shafa_do_city)
        shafa.add_command(label='词云图', command=self.shafa_do_word_cloud)
        shafa.add_command(label='销量售价图', command=self.shafa_do_sale_price)
        
        yizi = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='椅子', menu=yizi, underline=0)
        yizi.add_command(label='省分布图', command=self.yizi_do_pronvince)
        yizi.add_command(label='城市分布图', command=self.yizi_do_city)
        yizi.add_command(label='词云图', command=self.yizi_do_word_cloud)
        yizi.add_command(label='销量售价图', command=self.yizi_do_sale_price)



        baowenbei = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='保温杯', menu=baowenbei, underline=0) 
        baowenbei.add_command(label='省分布图', command=self.baowenbei_zuqiu_do_pronvince)
        baowenbei.add_command(label='城市分布图', command=self.baowenbei_do_city)
        baowenbei.add_command(label='词云图', command=self.baowenbei_do_word_cloud)
        baowenbei.add_command(label='销量售价图', command=self.baowenbei_do_sale_price)

'''
本作品由西南大学计信院杨远林所编写
版权归杨远林所有，违者必追究法律责任
最终解释权由杨远林决定
''''


        yijia = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='衣架', menu=yijia, underline=0) 
        yijia.add_command(label='省分布图', command=self.yijia_zuqiu_do_pronvince)
        yijia.add_command(label='城市分布图', command=self.yijia_do_city)
        yijia.add_command(label='词云图', command=self.yijia_do_word_cloud)
        yijia.add_command(label='销量售价图', command=self.yijia_do_sale_price)
        
        xiejia = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='鞋架', menu=xiejia, underline=0) 
        xiejia.add_command(label='省分布图', command=self.xiejia_do_pronvince)
        xiejia.add_command(label='城市分布图', command=self.xiejia_do_city)
        xiejia.add_command(label='词云图', command=self.xiejia_do_word_cloud)
        xiejia.add_command(label='销量售价图', command=self.xiejia_do_sale_price)


        canjinzi = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='餐巾纸', menu=canjinzi, underline=0) 
        canjinzi.add_command(label='省分布图', command=self.canjinzi_do_pronvince)
        canjinzi.add_command(label='城市分布图', command=self.canjinzi_do_city)
        canjinzi.add_command(label='词云图', command=self.canjinzi_do_word_cloud)
        canjinzi.add_command(label='销量售价图', command=self.canjinzi_do_sale_price)
        
        yahua = tk.Menu(jia_ju)
        jia_ju.add_cascade(label='牙刷', menu=yahua, underline=0) 
        yahua.add_command(label='省分布图', command=self.yahua_do_pronvince)
        yahua.add_command(label='城市分布图', command=self.yahua_do_city)
        yahua.add_command(label='词云图', command=self.yahua_do_word_cloud)
        yahua.add_command(label='销量售价图', command=self.yahua_do_sale_price)


    def xifashui_do_pronvince(self):
        a=CrawlProduct('洗发水','xifashui')
        #a.run(1)
        a.run(2)
    def xifashui_do_city(self):
        a=CrawlProduct('洗发水','xifashui')
        a.run(3)
    def xifashui_do_word_cloud(self):
        a=CrawlProduct('洗发水','xifashui')
        a.run(4)
    def xifashui_do_sale_price(self):
        a=CrawlProduct('洗发水','xifashui')
        a.run(5)        


        
    def xiangshui_do_pronvince(self):
        a=CrawlProduct('香水','xiangshui')
        #a.run(1)
        a.run(2)
    def xiangshui_do_city(self):
        a=CrawlProduct('香水','xiangshui')
        a.run(3)
    def xiangshui_do_word_cloud(self):
        a=CrawlProduct('香水','xiangshui')
        a.run(4)
    def xiangshui_do_sale_price(self):
        a=CrawlProduct('香水','xiangshui')
        a.run(5)

         
    def ximainnai_do_pronvince(self):
        a=CrawlProduct('洗面奶','ximainnai')
        #a.run(1)
        a.run(2)
    def ximainnai_do_city(self):
        a=CrawlProduct('洗面奶','ximainnai')
        a.run(3)
    def ximainnai_do_word_cloud(self):
        a=CrawlProduct('洗面奶','ximainnai')
        a.run(4)
    def ximainnai_do_sale_price(self):
        a=CrawlProduct('洗面奶','ximainnai')
        a.run(5)


    def muyulu_do_pronvince(self):
        a=CrawlProduct('沐浴露','muyulu')
        #a.run(1)
        a.run(2)
    def muyulu_do_city(self):
        a=CrawlProduct('沐浴露','muyulu')
        a.run(3)
    def muyulu_do_word_cloud(self):
        a=CrawlProduct('沐浴露','muyulu')
        a.run(4)
    def muyulu_do_sale_price(self):
        a=CrawlProduct('沐浴露','muyulu')
        a.run(5)  
   #-------------------------------------------------------------------------------------------------------------------------------------------------美妆模块-------------------------------------------------
    def   mei_zhuang(self):
       
        mei_zhuang = tk.Menu(self.menubar, tearoff=1)

        self.menubar.add_cascade(label='美妆  ', menu=mei_zhuang)
         

       
        xifashui = tk.Menu(mei_zhuang)
        mei_zhuang.add_cascade(label='洗发水', menu=xifashui, underline=0) 
        xifashui.add_command(label='省分布图', command=self.xifashui_do_pronvince)
        xifashui.add_command(label='城市分布图', command=self.xifashui_do_city)
        xifashui.add_command(label='词云图', command=self.xifashui_do_word_cloud)
        xifashui.add_command(label='销量售价图', command=self.xifashui_do_sale_price)

        
        xiangshui = tk.Menu(mei_zhuang)
        mei_zhuang.add_cascade(label='香水', menu=xiangshui, underline=0)
        xiangshui.add_command(label='省分布图', command=self.xiangshui_do_pronvince)
        xiangshui.add_command(label='城市分布图', command=self.xiangshui_do_city)
        xiangshui.add_command(label='词云图', command=self.xiangshui_do_word_cloud)
        xiangshui.add_command(label='销量售价图', command=self.xiangshui_do_sale_price)


        ximainnai = tk.Menu(mei_zhuang)
        mei_zhuang.add_cascade(label='洗面奶', menu=ximainnai, underline=0) 
        ximainnai.add_command(label='省分布图', command=self.ximainnai_do_pronvince)
        ximainnai.add_command(label='城市分布图', command=self.ximainnai_do_city)
        ximainnai.add_command(label='词云图', command=self.ximainnai_do_word_cloud)
        ximainnai.add_command(label='销量售价图', command=self.ximainnai_do_sale_price)



        muyulu = tk.Menu(mei_zhuang)
        mei_zhuang.add_cascade(label='沐浴露', menu=muyulu, underline=0) 
        muyulu.add_command(label='省分布图', command=self.muyulu_do_pronvince)
        muyulu.add_command(label='城市分布图', command=self.muyulu_do_city)
        muyulu.add_command(label='词云图', command=self.muyulu_do_word_cloud)
        muyulu.add_command(label='销量售价图', command=self.muyulu_do_sale_price)
        
    def xinglixiang_do_pronvince(self):
        a=CrawlProduct('行李箱','xinglixiang')
        #a.run(1)
        a.run(2)
    def xinglixiang_do_city(self):
        a=CrawlProduct('行李箱','xinglixiang')
        a.run(3)
    def xinglixiang_do_word_cloud(self):
        a=CrawlProduct('行李箱','xinglixiang')
        a.run(4)
    def xinglixiang_do_sale_price(self):
        a=CrawlProduct('行李箱','xinglixiang')
        a.run(5)



    def subao_do_pronvince(self):
        a=CrawlProduct('书包','subao')
        #a.run(1)
        a.run(2)
    def subao_do_city(self):
        a=CrawlProduct('书包','subao')
        a.run(3)
    def subao_do_word_cloud(self):
        a=CrawlProduct('书包','subao')
        a.run(4)
    def subao_do_sale_price(self):
        a=CrawlProduct('书包','subao')
        a.run(5)


    def yaobao_do_pronvince(self):
        a=CrawlProduct('腰包','yaobao')
        #a.run(1)
        a.run(2)
    def yaobao_do_city(self):
        a=CrawlProduct('腰包','yaobao')
        a.run(3)
    def yaobao_do_word_cloud(self):
        a=CrawlProduct('腰包','yaobao')
        a.run(4)
    def yaobao_do_sale_price(self):
        a=CrawlProduct('腰包','yaobao')
        a.run(5)


    def qianbao_do_pronvince(self):
        a=CrawlProduct('钱包','qianbao')
        #a.run(1)
        a.run(2)
    def qianbao_do_city(self):
        a=CrawlProduct('钱包','qianbao')
        a.run(3)
    def qianbao_do_word_cloud(self):
        a=CrawlProduct('钱包','qianbao')
        a.run(4)
    def qianbao_do_sale_price(self):
        a=CrawlProduct('钱包','qianbao')
        a.run(5)


  
                 
   #-------------------------------------------------------------------------------------------------------------------------------------------------箱包模块-------------------------------------------------
    def   xiang_bao(self):
       
        xiang_bao = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label='箱包  ', menu=xiang_bao)
         

       
        xinglixiang = tk.Menu(xiang_bao)
        xiang_bao.add_cascade(label='行李箱', menu=xinglixiang, underline=0) 
        xinglixiang.add_command(label='省分布图', command=self.xinglixiang_do_pronvince)
        xinglixiang.add_command(label='城市分布图', command=self.xinglixiang_do_city)
        xinglixiang.add_command(label='词云图', command=self.xinglixiang_do_word_cloud)
        xinglixiang.add_command(label='销量售价图', command=self.xinglixiang_do_sale_price)

        
        subao = tk.Menu(xiang_bao)
        xiang_bao.add_cascade(label='书包', menu=subao, underline=0)
        subao.add_command(label='省分布图', command=self.subao_do_pronvince)
        subao.add_command(label='城市分布图', command=self.subao_do_city)
        subao.add_command(label='词云图', command=self.subao_do_word_cloud)
        subao.add_command(label='销量售价图', command=self.subao_do_sale_price)


        yaobao = tk.Menu(xiang_bao)
        xiang_bao.add_cascade(label='腰包', menu=yaobao, underline=0) 
        yaobao.add_command(label='省分布图', command=self.yaobao_do_pronvince)
        yaobao.add_command(label='城市分布图', command=self.yaobao_do_city)
        yaobao.add_command(label='词云图', command=self.yaobao_do_word_cloud)
        yaobao.add_command(label='销量售价图', command=self.yaobao_do_sale_price)



        qianbao = tk.Menu(xiang_bao)
        xiang_bao.add_cascade(label='钱包', menu=qianbao, underline=0) 
        qianbao.add_command(label='省分布图', command=self.qianbao_do_pronvince)
        qianbao.add_command(label='城市分布图', command=self.qianbao_do_city)
        qianbao.add_command(label='词云图', command=self.qianbao_do_word_cloud)
        qianbao.add_command(label='销量售价图', command=self.qianbao_do_sale_price)


    def mubenhuahui_do_pronvince(self):
        a=CrawlProduct('木本花卉','mubenhuahui')
        #a.run(1)
        a.run(2)
    def mubenhuahui_do_city(self):
        a=CrawlProduct('木本花卉','mubenhuahui')
        a.run(3)
    def mubenhuahui_do_word_cloud(self):
        a=CrawlProduct('木本花卉','mubenhuahui')
        a.run(4)
    def mubenhuahui_do_sale_price(self):
        a=CrawlProduct('木本花卉','mubenhuahui')
        a.run(5)




    def guanyezhiwu_do_pronvince(self):
        a=CrawlProduct('观叶植物','guanyezhiwu')
        #a.run(1)
        a.run(2)
    def guanyezhiwu_do_city(self):
        a=CrawlProduct('观叶植物','guanyezhiwu')
        a.run(3)
    def guanyezhiwu_do_word_cloud(self):
        a=CrawlProduct('观叶植物','guanyezhiwu')
        a.run(4)
    def guanyezhiwu_do_sale_price(self):
        a=CrawlProduct('观叶植物','guanyezhiwu')
        a.run(5)




    def panyuanzhiwu_do_pronvince(self):
        a=CrawlProduct('攀岩植物','panyuanzhiwu')
        #a.run(1)
        a.run(2)
    def panyuanzhiwu_do_city(self):
        a=CrawlProduct('攀岩植物','panyuanzhiwu')
        a.run(3)
    def panyuanzhiwu_do_word_cloud(self):
        a=CrawlProduct('攀岩植物','panyuanzhiwu')
        a.run(4)
    def panyuanzhiwu_do_sale_price(self):
        a=CrawlProduct('攀岩植物','panyuanzhiwu')
        a.run(5)


    def shuishenziwu_do_pronvince(self):
        a=CrawlProduct('水生植物','shuishenziwu')
        #a.run(1)
        a.run(2)
    def shuishenziwu_do_city(self):
        a=CrawlProduct('水生植物','shuishenziwu')
        a.run(3)
    def shuishenziwu_do_word_cloud(self):
        a=CrawlProduct('水生植物','shuishenziwu')
        a.run(4)
    def shuishenziwu_do_sale_price(self):
        a=CrawlProduct('水生植物','shuishenziwu')
        a.run(5)



    def sicongziwu_do_pronvince(self):
        a=CrawlProduct('食虫植物','sicongziwu')
        #a.run(1)
        a.run(2)
    def sicongziwu_do_city(self):
        a=CrawlProduct('食虫植物','sicongziwu')
        a.run(3)
    def sicongziwu_do_word_cloud(self):
        a=CrawlProduct('食虫植物','sicongziwu')
        a.run(4)
    def sicongziwu_do_sale_price(self):
        a=CrawlProduct('食虫植物','sicongziwu')
        a.run(5)



    def meigui_do_pronvince(self):
        a=CrawlProduct('玫瑰','meigui')
        #a.run(1)
        a.run(2)
    def meigui_do_city(self):
        a=CrawlProduct('玫瑰','meigui')
        a.run(3)
    def meigui_do_word_cloud(self):
        a=CrawlProduct('玫瑰','meigui')
        a.run(4)
    def meigui_do_sale_price(self):
        a=CrawlProduct('玫瑰','meigui')
        a.run(5)


    def mudan_do_pronvince(self):
        a=CrawlProduct('牡丹','mudan')
        #a.run(1)
        a.run(2)
    def mudan_do_city(self):
        a=CrawlProduct('牡丹','mudan')
        a.run(3)
    def mudan_do_word_cloud(self):
        a=CrawlProduct('牡丹','mudan')
        a.run(4)
    def mudan_do_sale_price(self):
        a=CrawlProduct('牡丹','mudan')
        a.run(5)


    def lanhua_do_pronvince(self):
        a=CrawlProduct('兰花','lanhua')
        #a.run(1)
        a.run(2)
    def lanhua_do_city(self):
        a=CrawlProduct('兰花','lanhua')
        a.run(3)
    def lanhua_do_word_cloud(self):
        a=CrawlProduct('兰花','lanhua')
        a.run(4)
    def lanhua_do_sale_price(self):
        a=CrawlProduct('兰花','lanhua')
        a.run(5)
        


   #-------------------------------------------------------------------------------------------------------------------------------------------------花卉模块-------------------------------------------------
    def   hua_hui(self):
       
        hua_hui = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label='植物花卉  ',font=('Arial', 10), menu=hua_hui)
         

       
        mubenhuahui = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='木本花卉', menu=mubenhuahui, underline=0) 
        mubenhuahui.add_command(label='省分布图', command=self.mubenhuahui_do_pronvince)
        mubenhuahui.add_command(label='城市分布图', command=self.mubenhuahui_do_city)
        mubenhuahui.add_command(label='词云图', command=self.mubenhuahui_do_word_cloud)
        mubenhuahui.add_command(label='销量售价图', command=self.mubenhuahui_do_sale_price)

        
        guanyezhiwu = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='观叶植物', menu=guanyezhiwu, underline=0)
        guanyezhiwu.add_command(label='省分布图', command=self.guanyezhiwu_do_pronvince)
        guanyezhiwu.add_command(label='城市分布图', command=self.guanyezhiwu_do_city)
        guanyezhiwu.add_command(label='词云图', command=self.guanyezhiwu_do_word_cloud)
        guanyezhiwu.add_command(label='销量售价图', command=self.guanyezhiwu_do_sale_price)


        panyuanzhiwu = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='攀岩植物', menu=panyuanzhiwu, underline=0) 
        panyuanzhiwu.add_command(label='省分布图', command=self.panyuanzhiwu_do_pronvince)
        panyuanzhiwu.add_command(label='城市分布图', command=self.panyuanzhiwu_do_city)
        panyuanzhiwu.add_command(label='词云图', command=self.panyuanzhiwu_do_word_cloud)
        panyuanzhiwu.add_command(label='销量售价图', command=self.panyuanzhiwu_do_sale_price)



        shuishenziwu = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='水生植物', menu=shuishenziwu, underline=0) 
        shuishenziwu.add_command(label='省分布图', command=self.shuishenziwu_do_pronvince)
        shuishenziwu.add_command(label='城市分布图', command=self.shuishenziwu_do_city)
        shuishenziwu.add_command(label='词云图', command=self.shuishenziwu_do_word_cloud)
        shuishenziwu.add_command(label='销量售价图', command=self.shuishenziwu_do_sale_price)


        sicongziwu = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='食虫植物', menu=sicongziwu, underline=0) 
        sicongziwu.add_command(label='省分布图', command=self.sicongziwu_do_pronvince)
        sicongziwu.add_command(label='城市分布图', command=self.sicongziwu_do_city)
        sicongziwu.add_command(label='词云图', command=self.sicongziwu_do_word_cloud)
        sicongziwu.add_command(label='销量售价图', command=self.sicongziwu_do_sale_price)

        meigui = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='玫瑰', menu=meigui, underline=0) 
        meigui.add_command(label='省分布图', command=self.meigui_do_pronvince)
        meigui.add_command(label='城市分布图', command=self.meigui_do_city)
        meigui.add_command(label='词云图', command=self.meigui_do_word_cloud)
        meigui.add_command(label='销量售价图', command=self.meigui_do_sale_price)


        mudan = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='牡丹', menu=mudan, underline=0) 
        mudan.add_command(label='省分布图', command=self.mudan_do_pronvince)
        mudan.add_command(label='城市分布图', command=self.mudan_do_city)
        mudan.add_command(label='词云图', command=self.mudan_do_word_cloud)
        mudan.add_command(label='销量售价图', command=self.mudan_do_sale_price)

        lanhua = tk.Menu(hua_hui)
        hua_hui.add_cascade(label='兰花', menu=lanhua,font=('Arial', 20), underline=0) 
        lanhua.add_command(label='省分布图', command=self.lanhua_do_pronvince)
        lanhua.add_command(label='城市分布图', command=self.lanhua_do_city)
        lanhua.add_command(label='词云图', command=self.lanhua_do_word_cloud)
        lanhua.add_command(label='销量售价图', command=self.lanhua_do_sale_price)
                                                 

#-------------------------------------------------------------------------------------------------------------------------------------------------代理模块-------------------------------------------------

    def show_proxy(self):
        con = RdisClient()
        message=con.random()
        tk.messagebox.showinfo(title='当前代理为：', message=message)
    def show_CountProxy(self):
        con = RdisClient()
        count=con.count()
        tk.messagebox.showinfo(title='可用代理总数为：', message=count)  

    def get_proxy(self):
        get='权限不够'
        tk.messagebox.showinfo(title='代理数', message=get)  

    def   proxy(self):
        
        proxy = tk.Menu(self.menubar, tearoff=1)
        self.menubar.add_cascade(label='代理查看  ', menu=proxy)
        
        #show_proxy = tk.Menu(proxy)
        proxy.add_command(label='获取代理', command=self.get_proxy)
        proxy.add_command(label='当前代理', command=self.show_proxy)
        proxy.add_command(label='代理总数', command=self.show_CountProxy)          

    def autor(self):
        tk.messagebox.askokcancel('作者信息','本软件由杨远林开发')
    def about(self):
        tk.messagebox.askokcancel('版权信息.Copyright','本软件由杨远林团队所有')

    #添加版权子菜单
    def About(self):
        Aboutmenu=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='关于',menu=Aboutmenu)
        
        Aboutmenu.add_command(label='作者',command=self.autor)
        Aboutmenu.add_command(label='版权',command=self.about)
        
           

        
    def manege(self):
        # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
        self.show_photo()
    
        self.Labe()

        
        #热卖推荐
        ren_men_tui_quan()

        #体育
        PF()

        #服装
        fu_zhuang()

        
        #数码
       shu_ma()

        #美食
        mei_si()

        #家居
        self.jia_ju()

        #美妆
        mei_zhuang()

        #箱包
        xiang_bao()

        #花卉
        hua_hui()
        

        #查看代理
        proxy()


        #关于

        About()
        
        #tk.Label(self.window, text='dddd', bg='orange', font=('Arial', 10)).grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)
        #tk.Label(self.window, text='on the window', bg='red', font=('Arial', 10)).grid(row=7, column=1 ,padx=10, pady=10, ipadx=10, ipady=10)
        tk.Label(self.window, text='on the window', bg='red', font=('Arial', 16)).pack(side='left')
        file='F:\Python_chenxu\computer_prongram_contest\photo\demo1.gif'
        
        canvas = tk.Canvas(self.window, width=1350, height=700, bg='white')
        image_file = tk.PhotoImage(file=file)
        image = canvas.create_image(665, 6, anchor='n', image=image_file)#680,4适合n
        canvas.grid(row=0, column=0,sticky='n')



        '''
        tk.Label(self.window, text='欢迎来到淘宝数据可视化系统',bg='orange',font=('Arial', 30)).grid(row=8, column= 2)

        #列表框控件
        text=tk.Listbox(self.window, font=('Arial', 20),bg='white',width=65,height=15)
        text.grid(row=9,column=2)
        '''
        '''
        cv = tk.Canvas(self.window,bg = 'white',width=400, height=635)
        # 创建一个矩形，坐标为(10,10,110,110)
        cv.create_rectangle(10,10,110,110)
        cv.pack()
        '''
        self.window.config(menu=self.menubar)
         # 第12步，主窗口循环显示
        self.window.mainloop()
    
if __name__ == '__main__':
    a=GUI()
    a.manege()
    











        
        

'''
window = tk.Tk()
window.title('My Window')
'''
#windowWidth = 960               #获得当前窗口宽
#windowHeight = 640              #获得当前窗口高
#screenWidth,screenHeight = root.maxsize()     #获得屏幕宽和高
#geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
# 第3步，设定窗口的大小(长 * 宽)
'''
window.geometry('800x600')  # 这里的乘是小x
 
# 第4步，在图形界面上创建一个标签用以显示内容并放置
l = tk.Label(window, text='      ', bg='green')
l.pack()
 
# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1

def  do_city():
    a=YU_MAO_QIU()
    a.run(3)
def  do_pronvince():
    a=YU_MAO_QIU()
    a.run(2)
def  do_word_cloud():
    a=YU_MAO_QIU()
    a.run(4)
# 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
 
# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
PeMenu = tk.Menu(menubar, tearoff=1)

menubar.add_cascade(label='体育', menu=PeMenu)
 

#PeMenu.add_command(label='篮球', command=do_job)
lanqiu = tk.Menu(PeMenu)
PeMenu.add_cascade(label='篮球', menu=lanqiu, underline=0) # 给放入的菜单submenu命名为Import
lanqiu.add_command(label='省分布图', command=do_job)
lanqiu.add_command(label='城市分布图', command=do_job)
lanqiu.add_command(label='词云图', command=do_job)



zuqiu = tk.Menu(PeMenu)
PeMenu.add_cascade(label='足球', menu=zuqiu, underline=0) # 给放入的菜单submenu命名为Import
zuqiu.add_command(label='省分布图', command=do_job)
zuqiu.add_command(label='城市分布图', command=do_city)
zuqiu.add_command(label='词云图', command=do_word_cloud)


yumaoqiu = tk.Menu(PeMenu)
PeMenu.add_cascade(label='羽毛球拍', menu=yumaoqiu, underline=0) # 给放入的菜单submenu命名为Import
yumaoqiu.add_command(label='省分布图', command=do_pronvince)
yumaoqiu.add_command(label='城市分布图', command=do_city)
yumaoqiu.add_command(label='词云图', command=do_word_cloud)



bingbangqiu = tk.Menu(PeMenu)
PeMenu.add_cascade(label='兵乓球拍', menu=bingbangqiu, underline=0) # 给放入的菜单submenu命名为Import
bingbangqiu.add_command(label='省分布图', command=do_job)
bingbangqiu.add_command(label='城市分布图', command=do_job)
bingbangqiu.add_command(label='词云图', command=do_job)




PeMenu.add_command(label='足球', command=do_job)
PeMenu.add_command(label='羽毛球拍', command=do_job)
PeMenu.add_command(label='兵乓球拍', command=do_job)
#PeMenu.add_separator()    # 添加一条分隔线
#PeMenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数

def autor():
    tkinter.messagebox.askokcancel('作者信息','本软件由杨远林开发')
def about():
    tkinter.messagebox.askokcancel('版权信息.Copyright','本软件由杨远林团队所有')

#添加版权子菜单
Aboutmenu=tk.Menu(menubar)
Aboutmenu.add_command(label='作者',command=autor)
Aboutmenu.add_command(label='版权',command=about)
Aboutmenu.add_cascade(label='关于',menu=Aboutmenu)

'''






 

