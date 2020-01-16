#!/usr/bin/python

from configing import simple_userlogin

user_information = {
    "user_name": "admin",
    "domain": "leejay.vip",
    "server_host": "192.168.173.209"
}
simple_userlogin.simple_common_user_login(user_information)


