#!/usr/bin/python
import os
import datetime
import shutil

"""
此程序只实现了备份bin libexec lib64三个目录的功能
未完待续...
"""

coremail_home = "/home/coremail/"
backup_coremail_dir = "backup_coremail_dir/"
now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


def compress_to_targz(tar_name, coremail_dir):
    """
    compress coremail file to dir backup_coremail_dir/
    :param tar_name: compress file name
    :param coremail_dir: need compress coremail directory name
    :return:
    """

    tar_file_name = backup_coremail_dir + "coremail_{tar_name}_{time}".format(tar_name=tar_name, time=now)
    shutil.make_archive(tar_file_name, "zip", coremail_dir)
    print tar_file_name + " backup finish"


def backup_coremail_programs():
    """
    back up coremail direcory
    :return:
    """
    os.system("export COREMAIL_HOME=" + coremail_home)
    stop_coremail = os.system("%s/sbin/cmctrl.sh" % coremail_home + " stop")
    if stop_coremail == 0:
        print "Info: coremail system has already stop success"
        print "Info: begin backup coremail programs"
        if os.path.isdir(coremail_home + "/bin"):
            compress_to_targz("bin", coremail_home + "/bin")
        if os.path.isdir(coremail_home + "/libexec"):
            compress_to_targz("libexec", coremail_home + "/libexec")
        if os.path.isdir(coremail_home + "/lib64"):
            compress_to_targz("lib64", coremail_home + "/lib64")
        print "Info: backup coremail dir complete"
    else:
        print "\033[31;1mWarn:\033[0m coremail system is not stop"

def main():
    os.system("uname -a && cat /proc/version")
    system_version_ask = raw_input("Do the system version information is correct?(Y/N)")
    if system_version_ask.strip() == "Y" or system_version_ask.strip() == "y":
        backup_coremail_programs()
    else:
        print "\033[31;1mWarn:\033[0m The python script is not run"

if __name__ == "__main__":
    main()
