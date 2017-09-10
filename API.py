# -*- coding: utf-8 -*-

from DownLoadPic import *

def GenerateStuNum(college, year, major, classNum, stuNum):  # 生成学号
    college = str(college)
    year = str(year)
    major = str(major)
    classNum = str(classNum)
    stuNum = str(stuNum)
    if college.__len__() == 1:
        college = '0' + college
    if classNum.__len__() == 1:
        classNum = '0' + classNum
    if year.__len__() == 1:
        year = '0' + year
    if stuNum.__len__() == 1:
        stuNum = '0' + stuNum
    return college + year + major + classNum + stuNum


def DownLoadAll():  # 学院号两位，年段两位，专业号1位，班级号两位，学号2位
    for j in range(15, 17 + 1):  # 有待完善，如何及时跳出，避免无意义的网络访问
        for i in range(1, 17):
            for k in range(1, 10):
                for m in range(1, 10):
                    for n in range(1, 50):
                        if DownLoadPic(GenerateStuNum(i, j, k, m, n)) == 0 and DownLoadPic(GenerateStuNum(i, j, k, m, n+1)) == 0:
                            break


def DownLoadCollege(college, year):  # 下载某个学院
    for k in range(1, 10):
        for m in range(1, 10):
            for n in range(1, 50):
                if DownLoadPic(GenerateStuNum(college, year, k, m, n)) == 0 and DownLoadPic(GenerateStuNum(college, year, k, m, n+1)) == 0:
                    break


def DownLoadMajor(college, year, major):  # 下载某个专业
    for m in range(1, 10):
        for n in range(1, 50):
            if DownLoadPic(GenerateStuNum(college, year, major, m, n)) == 0 and DownLoadPic(GenerateStuNum(college, year, major, m, n+1)) == 0:
                break


def DownLoadClass(college, year, major, classNo):  # 下载某个班
    for n in range(1, 50):
        if DownLoadPic(GenerateStuNum(college, year, major, classNo, n)) == 0 and DownLoadPic(GenerateStuNum(college, year, major, classNo, n+1)) == 0:
            break


def DownLoadYear(year):
    for i in range(1, 17):
        for k in range(1, 10):
            for m in range(1, 10):
                for n in range(1, 50):
                    if DownLoadPic(GenerateStuNum(i, year, k, m, n)) == 0 and DownLoadPic(GenerateStuNum(i, year, k, m, n+1)) == 0:
                        break
