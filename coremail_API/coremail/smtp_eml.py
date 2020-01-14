import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "192.168.213.187"  # 设置服务器
mail_user = "admin@leejay.vip"  # 用户名
mail_pass = "1"  # 口令
receivers = ['cm3@leejay.vip']  # 接收邮件
rcpt_to = receivers[0]
i = 0
while i <= 5:
    i += 1
    message = MIMEText('Python 邮件发送测试%s...' %i, 'plain', 'utf-8')  #正文
    message['From'] = Header(mail_user, 'utf-8')  #正文里发件人信息
    message['To'] = Header(rcpt_to, 'utf-8')  #正文里的收件人

    subject = 'Python SMTP 邮件测试' + str(i) #标题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")