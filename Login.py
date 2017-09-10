# -*- coding: utf-8 -*-
import http.cookiejar
import urllib
from urllib import parse
from urllib import request
from urllib.error import URLError

def SaveCookie(usr,pwd):       #保存在cookie.txt
    loginUrl = "http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp"
    values = {}
    values['usr'] = usr
    values['pwd'] = pwd
    GET_data = urllib.parse.urlencode(values)
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate'}

    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)               # 自定义Opener对象

    geturl = loginUrl + "?" + GET_data                          # 构造访问网址
    try:
        request = urllib.request.Request(geturl, headers=headers)  # 构造包含headers的request
        response = opener.open(request)
    except URLError as e:
        print(e)
        return 0
    if cookie.__len__() == 1:
        return 2
    else:
        cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
        return 1



