from DownLoadPic import *
from Login import SaveCookie


def GenerateStuNum(college,year,major,classNum,stuNum):         #生成学号
    college = str(college)
    year = str(year)
    major = str(major)
    classNum = str(classNum)
    stuNum = str(stuNum)
    if college.__len__() == 1:
        college = '0'+college
    if classNum.__len__() == 1:
        classNum = '0'+classNum
    if year.__len__() == 1:
        year = '0'+year
    if stuNum.__len__() == 1:
        stuNum = '0'+stuNum
    return college+year+major+classNum+stuNum

def ListNumber(college = 1,year = 15,major = 1,classNum = 1,stuNum = 1):         #学院号两位，年段两位，专业号1位，班级号两位，学号2位
    # for j in range(year,17+1):
    #    for i in range(college, 17):
           for k in range(major,5):
               for m in range(classNum,5):
                   for n in range(stuNum,50):
                       if DownLoadPicPic(GenerateStuNum(college,year,k,m,n)) == 0:
                           break
SaveCookie()
ListNumber(16,15,4,2,1)
#ListNumber(16,15,4,2,1)
# if SaveCookie() ==0 :                        #获取cookie
#     exit()                                 #
# else:
#     print()        #爬取照片