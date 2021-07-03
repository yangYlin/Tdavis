'''
输入要爬取的网站连接，然后从redis库中选择代理ip进行测试
若通过测试则分数变为100，不通过则分数减1

'''
from RdisClient import RdisClient

import sys
import aiohttp
import asyncio
from asyncio import Queue
import time



VALID_STATUS_CODES = [200]#状态码 如果目标网站不同 可以更改
TEST_URL = 'http://www.SWU.edu.com' #测试网站
BATCH_TEST_SIZE = 10#批量测试最大值

class Tester(object):
    def __init__(self):
        
        
        self.redis = RdisClient()
        #检测单个代理的可用情况 async代表异步
    async def test_single_proxy(self, proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
            
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                    
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试', proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        #print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法 ', response.status, 'IP', proxy)
            except (aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)
    #测试主函数
    def manege(self):
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
               # print('正在测试第', start + 1, '-', stop, '个代理')
        
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)


a=Tester()

print(a.manege())







