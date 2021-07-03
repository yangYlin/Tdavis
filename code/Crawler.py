#获取模块

import json

#from .utils import get_page
from pyquery import PyQuery as pq
import requests

class ProxyMetaClass(type):
    def __new__(cls,name,bases,attrs):
        count=0
        attrs['__CrawlFunc__']=[]
        
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__CrawlFuncCount__']=count
        return type.__new__(cls,name,bases,attrs)


class Crawler(object,metaclass=ProxyMetaClass):
    def get_proxies(self,callback):
        proxies=[]
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取代理：',proxy)
            proxies.append(proxy)
        return proxies
    
    #从代理66上获取免费的IP
    def crawl_daili66(self,page_count=80):

        start_url='http://www.66ip.cn/{}.html'
        urls=[start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('爬取：',url)
            doc=pq(requests.get(url).text)
            trs=doc('.containerbox table tr:gt(0)').items()
            #print('开始爬！',trs)
            for tr in trs:
                ip=tr.find('td:nth-child(1)').text()
                port=tr.find('td:nth-child(2)').text()
                #print(ip)
                yield  ':'.join([ip,port])
            
            '''
            #html=get_page(url)
            if html:
                
                doc=pq(html)
                trs=doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip=tr.find('td:nth-child(1)').text()
                    port=tr.find('td:nth-child(2)').text()
                    yield  ':'.join(ip.port)
                    '''
    
'''       
a=Crawler()

for k in a.crawl_daili66():
    print(k)

   '''     
      

