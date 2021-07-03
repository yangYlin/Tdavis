﻿from flask import Flask, g
from RdisClient import RdisClient




__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RdisClient()
        return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'

@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    """
        Get the count of proxies
        :return: 代理池总量
     """
    conn = get_conn()
    return conn.count()
if __name__ == '__main__':
    app.run()
