## 思路
教务处个人信息url：http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp  
需要使用cookie登陆  
通过登陆地址：http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp?usr=&pwd=
得到cookie
获取图片要验证Referer  
response直接返回图片流

## 函数说明
### DownLoadAll()  
下载15-17级所以学生的照片  
### DownLoadCollege()
下载某个学院的学生照片
### DownLoadMajor()
下载某个专业的学生照片
### DownLoadClass()
下载某个班级的学生照片
