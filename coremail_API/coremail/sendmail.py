import time
import smtplib
import sys
import os

def sendMailTest(mail_sender, mail_passwd, mail_rcpts, rcpt_host, port):
    """
    : 发信
    :param mail_sender:  发件人
    :param mail_passwd:  密码
    :param mail_rcpts:  收件人
    :param rcpt_host:  服务器
    :return:
    """
    print(mail_sender)
    print(mail_passwd)
    print(mail_rcpts)
    print(rcpt_host)
    is_conn_timout = False
    to_mx = rcpt_host + ":" + port
    helo_domain = mail_sender.split('@')[1]
    enter_symbol = os.linesep
    msg = "From: {fromaddr}{enter_symbol}To: {toaddr}{enter_symbol}Subject: coremail SA team testing{enter_symbol}" \
          "{enter_symbol}This is not a fraud, so Don't panic{enter_symbol}" \
          "I can't send email to you ,so I try do some test{enter_symbol}" \
          "Please dont reply this mail , and{enter_symbol}" \
          "So Long, and Thanks for All the Fish.{enter_symbol}".format(
        fromaddr=mail_sender,
        toaddr=mail_rcpts,
        enter_symbol=enter_symbol
    )
    time_begin_conn = time.time()
    try:
        if port == "25":
            server = smtplib.SMTP(to_mx, timeout=180)
            server.starttls()  # 加密端口发信 不能带这个
        elif port == "465":
            server = smtplib.SMTP_SSL(to_mx, timeout=180)  # 加密端口发信得用 SMTP_SSL
        else:
            print("Warn: 端口出错" + port)
        time_end_conn = time.time()
    except Exception as e:
        print("连接收信方MX失败： %s" % str(e))
        sys.exit(1)
    server.set_debuglevel(1)
    time_begin_ehlo = time.time()
    server.ehlo(helo_domain)
    time_begin_mail_from = time.time()

    server.login(mail_sender, mail_passwd)   # 认证阶段
    server.mail(mail_sender)  # mail from阶段
    time_begin_rcpt = time.time()
    server.rcpt(mail_rcpts)  # rcpt 阶段
    time_begin_data = time.time()
    try:
        server.data(msg)
        # time_end_data = time.time()
    except Exception as e:
        print("mail cmd DATA failed:" + str(e))
        # time_end_data = time.time()
        is_conn_timout = True
        # server.close()
    time_end_data = time.time()
    if not is_conn_timout:
        server.quit()
    time_end_all = time.time()
    print("连接MX %s 阶段用时：%fs" % (str(rcpt_host), time_end_conn - time_begin_conn))
    print("HELO阶段用时：%fs" % (time_begin_mail_from - time_begin_ehlo))
    print("MAIL FROM 阶段用时：%fs" % (time_begin_rcpt - time_begin_mail_from))
    print("MAIL RCPT 阶段用时：%fs" % (time_begin_data - time_begin_rcpt))
    print("MAIL DATA 阶段用时：%fs" % (time_end_data - time_begin_data))
    print("整个发信用时： %fs" % (time_end_all - time_begin_conn))

def main():
    mail_from = "test23@fudan.edu.cn"
    mail_passwd = "coremail123"
    mail_to = "yunpeng.long@modelorg.com"
    # mail_to = "test23@fudan.edu.cn"
    mx_host = "10.5.5.93"

    # 25端口发信
    # sendMailTest(mail_sender=mail_from, mail_passwd=mail_passwd, mail_rcpts=mail_to, rcpt_host=mx_host, port="25")

    # 465端口发信
    sendMailTest(mail_sender=mail_from, mail_passwd=mail_passwd, mail_rcpts=mail_to, rcpt_host=mx_host, port="465")

if __name__ == "__main__":
    main()
