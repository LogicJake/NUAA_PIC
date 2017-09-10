# -*- coding: utf-8 -*-
import http.cookiejar
import urllib
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup

def SaveCookie():       #保存在cookie.txt
    loginUrl = "http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp"
    values = {}
    values['usr'] = "161540208"
    values['pwd'] = "St106012"
    GET_data = urllib.parse.urlencode(values)
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate'}

    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)               # 自定义Opener对象

    geturl = loginUrl + "?" + GET_data                          # 构造访问网址
    request = urllib.request.Request(geturl, headers=headers)   #  构造包含headers的request
    response = opener.open(request)
    #print(response.read())
    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

def DownLoadPicPic(xh,pic = "xh"): # 利用cookie.txt中的cookie访问http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)      # 加载cookie
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent,
               'Connection': 'keep-alive',
               'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
               'Accept-Encoding':'zh-CN,zh;q=0.8',
               'Referer':'http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp'}

    get_url = "http://ded.nuaa.edu.cn/netean/GetPic.asp"

    values = {}
    values['pic'] = pic
    values['xh'] = xh
    GET_data = urllib.parse.urlencode(values)
    get_url += "?" + GET_data

    get_request = urllib.request.Request(get_url,headers=headers)
    get_response = opener.open(get_request)

    fhand = open('./PIC/'+xh+'.jpg', 'wb')
    size = 0
    while True:
        info = get_response.read(100000)
        if len(info) < 1: break
        size = size + len(info)
        fhand.write(info)


