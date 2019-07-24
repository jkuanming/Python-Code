import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header 

#定义变量
username = input('请输入你的邮箱账号:') #'jkuanming@qq.com'
password = input('请输入你的邮箱密码:') #'gsmykrjxvpazcace'
from_addr = input('请输入你的发件人邮箱地址:') #'jkuanming@qq.com'

to_addrs = []
while True:
    a=input('请输入收件人邮箱：')
    #输入收件人邮箱
    to_addrs.append(a)
    #写入列表
    b=input('是否继续输入，n退出，任意键继续：')
    #询问是否继续输入
    if b == 'n':
        break
print(to_addrs)

smtp_server = 'smtp.qq.com'
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header('阿宽')
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('hello python world')

#开启发信服务
#以下两行为默认不加密的端口25链接邮箱服务器的方法
'''server = smtplib.SMTP()           
server.connect(smtp_server, 25) '''  
#以下两行为加密SSL端口465链接邮箱服务器的方法
server = smtplib.SMTP_SSL(smtp_server)  #如果端口是用SSL加密，请这样写代码。其中server是变量名
server.connect(smtp_server,465)         #如果出现编码错误UnicodeDecodeError，你可以这样写：server.connect('smtp.qq.com', 465,'utf-8')

#登陆发信邮箱
server.login(username, password) 

#发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())

#关闭邮箱服务
server.quit() 