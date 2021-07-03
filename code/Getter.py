from RdisClient import RdisClient
from Crawler import Crawler

#代理池最大数量
MAX= 2000


class Getter():
    

    def __init__(self):
        self.redis = RdisClient()
        self.crawler = Crawler()
        #判断代理池是否到了阀值
    def is_full(self):
            #判断是否达到了代理池限制
        if self.redis.count() >= MAX:
            return True
        else:
            return False
	#print( self.redis.count() )
    def run(self):
        #print('获取器开始执行')
        # 判断代理池是否到了阀值
        if not self.is_full():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback =self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies =self.crawler.get_proxies(callback)
                #print('proxies',proxies)
                #sys.stdout.flush()
                for proxy in proxies:
                    #添加数据库
                    print('添加数据库',proxy)
                    self.redis.add(proxy)


a=Getter()
a.run()
