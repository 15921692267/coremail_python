#!/usr/bin/python
# _*_ coding:utf-8 _*_
import os
import re

def get_ip4_address():
    """
    get centos system ip address
    :return:
    """
    ip_1 = os.popen("ifconfig").readlines()
    # print ip_1[1]
    ip_address = re.split(" ", ip_1[1])[9]
    return ip_address

def get_user_sessionID(email_address):
    """
    get user session id
    :param user_information: user information
    :return:
    """
    sid_return = os.popen("/home/coremail/bin/userutil --call-api cmd=5\&user_at_domain={email_address}"
                          .format(email_address=email_address)).readlines()
    #print sid_return[0]
    sid_split = re.split("chars\)", sid_return[0])
    sid = re.split(os.linesep, sid_split[1])
    return sid[0]

def get_user_cos_id(user_at_domain, org_id):
    """
    get user cos_id
    :param user_at_domain: eg: lijie@leejay.vip
    :param org_id:  eg: a
    :return:
    """
    os.system(
        "/home/coremail/bin/userutil --call-api \"cmd=3\&user_at_domain={user_at_domain}&org_id={org_id}\"  cos_id".format(
            user_at_domain=user_at_domain, org_id=org_id))

def create_user(user_at_domain, org_id, cos_id, true_name, user_passwd):
    """
    create user
    :param user_at_domain:
    :param org_id:
    :param cos_id:
    :param true_name:
    :param user_passwd:
    :return:
    """
    os.system(
        "/home/coremail/bin/userutil --call-api 'cmd=0&user_at_domain={user_at_domain}&org_id={org_id}' 'cos_id={cos_id}&password={user_passwd}&true_name={true_name}'".format(
            user_at_domain=user_at_domain,
            org_id=org_id,
            cos_id=cos_id,
            user_passwd=user_passwd,
            true_name=true_name
        ))

def get_AD_user_information(ad_ip, ad_user_login, ad_user_login_passwd, ad_bumen, ad_second_domain, ad_first_domain, ad_user_name):
    """
    验证AD域控用户信息 测试连接域控是否正常
    :param ad_ip: 域控的IP
    :param user_at_domain: 域控的登陆用户 eg:administrator@test.cn
    :param user_passwd: 域控用户的密码  eg:123456
    :param bumen: 域控上的部门  eg:leejay_IT
    :param second_domain: 二级域名 eg: test
    :param first_domain: 一级域名  eg: cn
    :param ad_user_name: 查询域控上的用户的信息 user_a2
    :return:
    """
    os.system("ldapsearch -p 389 -h {ad_ip} -D \"{ad_user_login}\" -w \"{ad_user_login_passwd}\" -b \"OU={ad_bumen},DC={ad_second_domain},DC={ad_first_domain}\" -x 'sAMAccountName={ad_user_name}'".format(
        ad_ip=ad_ip,
        ad_user_login=ad_user_login,
        ad_user_login_passwd=ad_user_login_passwd,
        ad_bumen=ad_bumen,
        ad_second_domain=ad_second_domain,
        ad_first_domain=ad_first_domain,
        ad_user_name=ad_user_name
    ))

def get_vitual_bumen_list(org_id):
    os.system("/home/coremail/bin/sautil call-api \"cmd=GET_HIERARCHY&org_id={org_id}\" --attrs=\"email\" | tee -a /tmp/virtual_bumen_list`date +%F`.txt".format(org_id=org_id))

def change_user_passwd(user_at_domain, org_id, new_passwd):
   os.system("/home/coremail/bin/userutil --call-api \"cmd=1\&user_at_domain={user_at_domain}&org_id={org_id}\" \"password={new_passwd}\"".format(
       user_at_domain=user_at_domain,
       org_id=org_id,
       new_passwd=new_passwd
   ))

msg_information = """
    0. 退出程序
    1. 显示所有的org_id 
    2. 普通用户单点
    3. 管理员单点
    4. 获取用户的服务等级cos_id
    5. 创建用户
    6. 验证AD域控用户信息
    7. 获取虚拟部门列表
    8. 修改用户的密码
"""
while True:
    print msg_information
    number_choice_ask = raw_input("\033[35;1mPlease input number:\033[0m ")
    if number_choice_ask == "0".strip():
        break
    if number_choice_ask == "1".strip():
        os.system("/home/coremail/bin/userutil --call-api \"cmd=43\"")
    if number_choice_ask == "2".strip():
        mail_host = get_ip4_address()
        email_address = raw_input("\033[34;1mPlease input user_at_domain:\033[0m ")
        sid = get_user_sessionID(email_address)
        print "http://{mail_host}/coremail/main.jsp?sid={sid}".format(mail_host=mail_host, sid=sid)
    if number_choice_ask == "3".strip():
        mail_host = get_ip4_address()
        email_address = raw_input("\033[34;1mPlease input user_at_domain:\033[0m ")
        sid = get_user_sessionID(email_address)
        print "http://{mail_host}/webadmin/~{sid}/~/usr/index_usr.jsp".format(mail_host=mail_host, sid=sid)
    if number_choice_ask == "4".strip():
        user_at_domain = raw_input("\033[34;1mPlease input user_at_domain:\033[0m ")
        org_id = raw_input("\033[34;1mPlease input org_id:\033[0m ")
        get_user_cos_id(user_at_domain, org_id)
    if number_choice_ask == "5".strip():
        user_at_domain = raw_input("\033[34;1mPlease input user_at_domain:\033[0m ")
        org_id = raw_input("\033[34;1mPlease input org_id:\033[0m ")
        cos_id = raw_input("\033[34;1mPlease input cos_id:\033[0m ")
        user_passwd = raw_input("\033[34;1mPlease input password:\033[0m ")
        true_name = raw_input("\033[34;1mPlease input true_name:\033[0m ")
        create_user(user_at_domain=user_at_domain, org_id=org_id, cos_id=cos_id, user_passwd=user_passwd, true_name=true_name)
    if number_choice_ask == "6".strip():
        ad_ip = raw_input("Please input AD server ip: ")
        ad_user_login = raw_input("Please input AD login user: ")
        ad_user_login_passwd = raw_input("Please input user passwd: ")
        ad_bumen = raw_input("Please input AD bumen: ")
        ad_second_domain = raw_input("Please input ad second domain: ")
        ad_first_domain = raw_input("Please input ad first domain: ")
        ad_user_name = raw_input("Please input ad auth user name: ")
        get_AD_user_information(ad_ip, ad_user_login, ad_user_login_passwd, ad_bumen, ad_second_domain, ad_first_domain, ad_user_name)
    if number_choice_ask == "7".strip():
        org_id = raw_input("\033[34;1mPlease input org_id:\033[0m ")
        get_vitual_bumen_list(org_id)
    if number_choice_ask == "8".strip():
        user_at_domain = raw_input("\033[34;1mPlease input user_at_domain:\033[0m ")
        org_id = raw_input("\033[34;1mPlease input org_id:\033[0m ")
        new_passwd = raw_input("\033[34;1mPlease input user new password:\033[0m ")
        change_user_passwd(user_at_domain, org_id, new_passwd)







# print "Info: 获取虚拟部门列表"
# os.system('/home/coremail/bin/sautil call-api "cmd=GET_HIERARCHY&org_id=a" --attrs="email"')

#print "Info: 获取动态邮件列表中的用户"
#email_list = "all_maillist_filter@leejay.vip"
#os.system("/home/coremail/bin/userutil --get-user-attr {email_list} maillist_filter".format(email_list=email_list))

#print "Info: 获取静态邮件列表中的用户"
#os.system("/home/coremail/bin/userutil --display {email_list} |grep forwardmaillist".format(email_list=email_list))
