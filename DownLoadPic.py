from Login import SaveCookie
from Login import LoginWithCookie
from urllib import request
def DownLoadPic(picurl):
    request.urlretrieve(picurl, "./pic/1.jpg")

SaveCookie()
LoginWithCookie()
DownLoadPic("http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh=161540208")