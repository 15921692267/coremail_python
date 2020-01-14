
# -*- coding:utf-8 -*-
import smtplib

to_mx = "mta6.am0.yahoodns.net." + ":25"
fromaddr = 'gjzc@fudan.edu.cn'
toaddrs  = ['test100@yahoo.com.cn']
msg = '''
    From: {fromaddr}
    To: {toaddr}
    Subject: testing'
    This is a test
    .
'''

msg = msg.format(fromaddr =fromaddr, toaddr = ','.join(toaddrs))
# The actual mail send
print("开始发信到 test100@yahoo.com.cn")
server = smtplib.SMTP(to_mx)
server.set_debuglevel(1)
server.ehlo("fudan.edu.cn")
server.mail(fromaddr)
for username in toaddrs:
    server.rcpt(username)
server.data(msg)
server.quit()