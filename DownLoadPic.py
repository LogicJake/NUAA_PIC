# -*- coding: utf-8 -*-
import http.cookiejar
import urllib
from urllib import parse
from urllib import request
from urllib.error import URLError
import os

def checkDir(pic):
    college = pic[0:2]
    year = pic[2:4]
    classNum = pic[4:7]
    if not os.path.exists("."+os.sep+college+"院"+ os.sep+year+"级"+ os.sep+classNum+os.sep):
        if not os.path.exists("."+os.sep+college+"院"):
            os.mkdir("." + os.sep + college + "院" + os.sep)
        if not os.path.exists("."+os.sep+college+"院"+ os.sep+year+"级"):
            os.mkdir("." + os.sep + college + "院" + os.sep + year + "级" + os.sep)
        os.mkdir("." + os.sep + college + "院" + os.sep + year + "级" + os.sep + classNum + os.sep)

def DownLoadPic(xh,pic = "xh"): # 利用cookie.txt中的cookie访问http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp
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

    try:
        get_request = urllib.request.Request(get_url, headers=headers)
        get_response = opener.open(get_request)
    except URLError as e:
        print(e)
        return 0

    checkDir(xh)       #生成对应的文件夹
    fhand = open('./' + str(xh[0:2]) + '院/' + str(xh[2:4]) + "级/" + str(xh[4:7]) + "/" + xh + '.jpg', 'wb')
    size = 0
    while True:
        info = get_response.read(100000)
        if len(info) < 1: break
        size = size + len(info)
        fhand.write(info)
    return 1