#!/usr/bin/python

import os

def modify_selinux_config():
    selinux_conf = open("/etc/selinux/config", "r+")
    for line in selinux_conf:
        # print line
        if "SELINUX=enforcing" in line:
            line = line.replace("enforcing", "disabled")
        selinux_conf.write(line)
    selinux_conf.close()

def main():
    """
    Install coremail system is need initialization el7_64 system
    :return:
    """
    os.system("uname -a && cat /proc/version")
    stop_firewalld = os.system("systemctl stop firewalld")
    if stop_firewalld == 0:
        print "Info: firewalld has already stop"

    disable_firewalld = os.system("systemctl disable firewalld")
    if disable_firewalld == 0 :
        print "Info: firewalld has alreadyll disabled"

    os.system("systemctl stop postfix")
    os.system("systemctl disable postfix")
    print "Info: postfix has already stop"

    os.system("setenforce 0")
    print "Info: selinux run status: "
    os.system("getenforce")

    backup_selinuxconf_ask = raw_input("Do you want to backup selinux config file?(Y/N)")
    if backup_selinuxconf_ask == "Y" or backup_selinuxconf_ask == "y":
        os.system("cp -a /etc/selinux/config{,.bak`date +%F_%H%M%S`}")
        print "Info: backup selinux config success"
        modify_selinux_config()
        print "Info: selinux has been modified"
    else:
        print "Info: selinux config is not backup and modify"
if __name__ == "__main__":
    main()