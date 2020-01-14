#!/usr/bin/python

import os

coremail_home = "/home/coremail"
confutil = coremail_home + "/bin/confutil"  # 修改coremail配置文件
coremail_mysql = coremail_home + "/bin/mysql_cm"  # 连接数据库

def restart_service():
    """
    :重启 tomcat nginx udsvr
    :return:
    """
    question = raw_input("restart tomcat nginx udsvr?(y/n):")
    if question == 'y':
        os.system(coremail_home + "/bin/coremail restart tomcat nginx udsvr")


def add_func():
    """
    :修改配置文件 添加二次验证的功能
    :return:
    """
    try:
        print("deploy in userschema.cf")
        os.system(confutil + "  --update " + coremail_home + "/conf/userschema.cf cm_user_pref_ext/bindauthkey=\"int\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/userschema.cf cm_user_pref_ext/authkeyid=\"string(80)\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/userschema.cf cm_user_bin_data/otp_history=\"struct(4000)\"")
        os.system(confutil + "  --upload userschema")

        # 在mysql数据库表中增加二次验证的字段
        print("deploy in DB")
        os.system(coremail_mysql + " cmxt -e \"alter table cm_user_pref_ext add authkeyid varchar(80);\"")
        os.system(coremail_mysql + " cmxt -e \"alter table cm_user_pref_ext add bindauthkey int;\"")
        os.system(coremail_mysql + " cmxt -e \"alter table cm_user_bin_data add otp_history blob;\"")

        print("deploy in policy.cf")
        os.system(
            confutil + "  --update " + coremail_home + "/conf/policy.cf global/ClientAuthType=\"web:base,dynamic\"")
        os.system(confutil + "  --upload policy")

        # 修改authkey.cf配置文件 增加二次验证的配置
        print("deploy in authkey.cf")
        os.system(
            confutil + "  --update " + coremail_home + "/conf/authkey.cf global/ConnStr=\"http://ukey.icoremail.net:18080/cbsite/authsys/api/verify/?app=coremail&appuser=$user$&user=sn-$usbkeyid$&pw=$passwd$\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf global/FixSlash=\"false\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf global/Method=\"get\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf global/AuthFlag=\"0\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf otpauth/verifyType=\"hmac-sha1\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf otpauth/Digits=\"6\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf otpauth/Interval=\"30\"")
        os.system(confutil + "  --update " + coremail_home + "/conf/authkey.cf otpauth/Windows=\"6\"")
        os.system(confutil + "  --upload authkey")

        # 增加二次验证向我司ukey.icoremail.net传参
        print("deploy in webmail.cf")
        os.system(
            confutil + "  --update " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalBindURL=\"http://ukey.icoremail.net:18080/cbsite/authsys/api/bind?app=coremail&appuser=$user$&user=sn-$usbkeyid$&pw=$passwd$\"")
        os.system(
            confutil + "  --update " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalUnbindURL=\"http://ukey.icoremail.net:18080/cbsite/authsys/api/bind?app=coremail&appuser=$user$&user=sn-$usbkeyid$&pw=$passwd$\"")
        os.system(
            confutil + "  --update " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalForceUnbindURL=\"http://ukey.icoremail.net:18080/cbsite/authsys/api/bind?app=coremail&appuser=$user$&user=sn-$usbkeyid$&pw=$passwd$\"")
        os.system(confutil + "  --upload webmail")
    except:
        raise


def del_func():
    """
    :删除 add_func() 中增加的配置
    :return:
    """
    try:
        print("deploy in userschema.cf")
        os.system(confutil + "  --remove " + coremail_home + "/conf/userschema.cf cm_user_pref_ext/bindauthkey")
        os.system(confutil + "  --remove " + coremail_home + "/conf/userschema.cf cm_user_pref_ext/authkeyid")
        os.system(confutil + "  --remove " + coremail_home + "/conf/userschema.cf cm_user_bin_data/otp_history")
        os.system(confutil + "  --upload userschema")

        # print("deploy in DB")
        # os.system(coremail_mysql + " cmxt -e \"alter table cm_user_pref_ext add authkeyid varchar(80);\"")
        # os.system(coremail_mysql + " cmxt -e \"alter table cm_user_pref_ext add bindauthkey int;\"")
        # os.system(coremail_mysql + " cmxt -e \"alter table cm_user_bin_data add otp_history blob;\"")

        print("deploy in policy.cf")
        os.system(confutil + "  --remove " + coremail_home + "/conf/policy.cf global/ClientAuthType")
        os.system(confutil + "  --upload policy")

        print("deploy in authkey.cf")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf global/ConnStr")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf global/FixSlash")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf global/Method")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf global/AuthFlag")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf otpauth/verifyType")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf otpauth/Digits")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf otpauth/Interval")
        os.system(confutil + "  --remove " + coremail_home + "/conf/authkey.cf otpauth/Windows")
        os.system(confutil + "  --upload authkey")

        print("deploy in webmail.cf")
        os.system(confutil + "  --remove " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalBindURL")
        os.system(confutil + "  --remove " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalUnbindURL")
        os.system(confutil + "  --remove " + coremail_home + "/conf/webmail.cf addon/authkey/ExternalForceUnbindURL")
        os.system(confutil + "  --upload webmail")
    except:
        raise


if __name__ == "__main__":
    try:
        if os.path.exists(coremail_home):
            if os.path.exists(confutil):
                if os.getcwd() == "/home/coremail/conf":
                    print "1.add func"
                    print
                    "2.del func"
                    print
                    "3.update func"
                    choice = raw_input("Input your choice:")
                    num = int(choice.strip())
                    if num == 1:
                        add_func()
                    elif num == 2:
                        del_func()
                    else:
                        print
                        "Error choice"
                else:
                    print
                    "This tool must work in /home/coremail/conf"
            else:
                print
                "This tool need confutil"
        else:
            print
            "This tool work for coremail"

    except ValueError:
        print
        "Error input, must number"
    except KeyboardInterrupt:
        print
        "\nError key input, Bye"


