from API import *
from Login import SaveCookie

usr = input("请输入您的学号:")
pwd = input("请输入教务处密码：")
res = SaveCookie(usr,pwd)
if  res == 0: # 访问获取cookie
    print("网络错误")
elif res == 2:
    print("密码错误")
elif res == 1:      #登陆成功
    if usr == "161540208":      #管理员身份
        admin = 1
        print("1.下载某个专业\t2.下载某个学院\t3.下载某个年级\t4.下载某个班\t5.下载某个人\t6.下载所有\n")
    else:
        admin = 0
        print("1.下载某个专业\t2.下载某个学院\t3.下载某个年级\t4.下载某个班\t5.下载某个人\n")
    choose = input("请输入您的选择:")
    if choose == "1":
        college = input("请输入学院号:")
        year = input("请输入年级:")
        major = input("请输入专业编号:")
        DownLoadMajor(college, year, major)
    elif choose == "2":
        college = input("请输入学院号:")
        year = input("请输入年级:")
        DownLoadCollege(college, year)
    elif choose == "3":
        year = input("请输入年级:")
        DownLoadYear(year)
    elif choose == "4":
        college = input("请输入学院号:")
        year = input("请输入年级:")
        major = input("请输入专业编号:")
        classNo = input("请输入班号:")
        DownLoadClass(college, year, major, classNo)
    elif choose == "5":
        stuNo = input("请输入学号:")
        DownLoadPic(stuNo)
    elif choose == "6" & admin == 1:
        DownLoadAll()