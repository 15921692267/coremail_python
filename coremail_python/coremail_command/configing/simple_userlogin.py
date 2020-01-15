#!/usr/bin/python

import os
import re

def simple_common_user_login(user_information):
    mail_host = "192.168.173.209"
    sid_return = os.popen("/home/coremail/bin/userutil --call-api cmd=5\&user_at_domain={user_name}"
                          .format(user_name=user_information["user_name"])).readlines()
    #print sid_return[0]
    sid_split = re.split("chars\)", sid_return[0])
    sid = re.split(os.linesep, sid_split[1])
    print "Info: webmail user {user_name} simple point login".format(user_name=user_information["user_name"])
    print "http://{mail_host}/coremail/main.jsp?sid={sid}".format(mail_host=user_information["host"], sid=sid[0])

    print "----------------"
    print "Info: webadmin {user_name} simple point login".format(user_name=user_information["user_name"])
    print "http://{mail_host}/webadmin/~{sid}/~/usr/index_usr.jsp".format(mail_host=mail_host, sid=sid[0])

