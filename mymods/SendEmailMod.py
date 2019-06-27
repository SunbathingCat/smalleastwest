import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可

# 设置完这三项即可使用该模块
Sender = '3014957624@qq.com'    # 发件人
Username = '3014957624@qq.com'  # 最好和发件人一样
Password = '一个授权码字符串，不是登录密码'    # 打开smtp服务时得到的授权码


def SendToOther(targit,title,body):
    # 发件人和收件人
    sender = Sender
    receiver = targit

    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.qq.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = Username
    password = Password

    mail_title = title
    mail_body = body

    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        smtp.quit()
        return 1
    except smtplib.SMTPException:
        return 0
def SendToMe(title,body):
    # 发件人和收件人
    sender = Sender
    receiver = Sender

    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.qq.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = Username
    password = Password

    mail_title = title
    mail_body = body

    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        smtp.quit()
        return 1
    except smtplib.SMTPException:
        return 0
def SendZipToOther(targit,title,body,zip):
    # 发件人和收件人
    sender = Sender
    receiver = targit

    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.qq.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = Username
    password = Password

    mail_title = title
    textApart = MIMEText(body)
    zipFile = zip
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=('utf-8','',zipFile))

    # 创建一个实例
    message = MIMEMultipart()
    message.attach(textApart)
    message.attach(zipApart)
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        smtp.quit()
        return 1
    except smtplib.SMTPException:
        return 0
