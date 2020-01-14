# from split_request_url import api_interface
from conf import split_request_url
import re
"""
attrs=后面的等号和&号都要用下面的字符 attrs 参数传递，并且 attrs 参数中的 = 和 & 要转成 url 编码
= 对应 %3D
& 对应 %26
api_interface() # 调用这个函数返回一个元组：一个返回码 一个api调用返回的结果
"""
def getAttrs_Method(coremail_user_infomation):
    """
    :获取用户信息
    :mbox_msgcnt 所有文件夹下的邮件总数
    :mbox_msgsize  邮件大小
    :mbox_newmsgcnt  所有文件夹下的未读邮件数
    :box_newmsgsize  未读邮件大小
    :mbox.folder.1.newmsgcnt  收件箱下的未读邮件数，其中数字“1”为收件箱的fid，替换为其他fid即可查询对应文件夹下的未读邮件数
    :param coremail_user_infomation:  用户信息字典
    :return:
    """
    user_attrs = 'user_at_domain={user_id}@{domain_name}&attrs=true_name%26domain_name%26' \
                 'path%26second_auth_type%26password%26password_expiry_time%26mbox_id%26nick_name%26user_id%26second_auth_type%26' \
                 'mbox_msgcnt%26mbox_msgsize%26mbox_newmsgcnt%26mbox_newmsgsize%26mbox.folder.1.newmsgcnt'.format(
                 user_id=coremail_user_infomation["coremail_user"],
                 domain_name=coremail_user_infomation["domain_name"])
    api_return_result = list(split_request_url.api_interface("getAttrs", user_attrs))
    get_user_result_list = re.split("&amp;", api_return_result[1])
    if api_return_result[0] == "0":
        for personal_user_attr_value in get_user_result_list:
            print(personal_user_attr_value)
    else:
        print("\033[31;1mWarn:\033[0m 用户 " + coremail_user_infomation["coremail_user"] + " 不存在:")
        print(api_return_result)

def getNewMailInfos_Method(coremail_user_infomation):
    """
    :获取用户未读邮件列表
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}&options=doubleDecode%3DTrue".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"]
    )
    api_return_result = list(split_request_url.api_interface("getNewMailInfos", coremail_user_attr))
    if api_return_result[0] == "0":
        api_return_result_split_list = re.split("%26", api_return_result[1])
        print(coremail_user_infomation["coremail_user"] + " 的未读邮件列表:")
        for mail_list in api_return_result_split_list:
            mail_list = mail_list.replace("%3D", "=")
            mail_list = mail_list.replace("&amp;", "\n")
            print(mail_list)
    else:
        print("\033[31;1mWarn:\033[0m 获取用户 " + coremail_user_infomation["coremail_user"] + " 未读邮件数失败:")
        print(api_return_result)

def get_deleteMailInfos_Method(coremail_user_infomation):
    """
    :删除邮件
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "uid={coremail_user}@{domain_name}&options=mid=1tbiAQELAlyd1qcACQALs7".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"]
    )
    api_return_result = split_request_url.api_interface("deleteMailInfos", coremail_user_attr)
    if api_return_result[0] == "0":
        print("删除邮件成功")
    else:
        print("删除邮件报错:")
        print(api_return_result)

def get_userExist_Method(coremail_user_infomation):
    """
    :判断用户是否存在
    :param coremail_user_infomation:   用户信息字典
    :return:
    """
    user_exist_attr = "user_at_domain=%s@%s" % (
                       coremail_user_infomation["coremail_user"],
                       coremail_user_infomation["domain_name"])
    api_return_result = split_request_url.api_interface("userExist", user_exist_attr)
    if api_return_result[0] == "0":
        print("Info: 用户 " + coremail_user_infomation["coremail_user"] + " 存在: " + api_return_result[1])
    else:
        print("\033[31;1mWarn:\033[0m 用户 " + coremail_user_infomation["coremail_user"] + " 不存在:")
        print(api_return_result)

def get_createUser_Method(coremail_user_infomation):
    """
    :创建用户
    :param coremail_user_infomation: 用户信息字典
    :return:
    """
    create_user_attr = "provider_id={provider_id}&org_id={org_id}&user_id={create_user_id}&" \
                       "attrs=domain_name%3Dleejay.vip%26user_status%3D{user_status}%26cos_id%3D{cos_id}" \
                       "%26quota_delta%3D0%26true_name%3D{true_name}%26password%3D{password}%26org_unit_id%3D{org_unit_id}".format(
                        provider_id=coremail_user_infomation["provider_id"],
                        org_id=coremail_user_infomation["org_id"],
                        create_user_id=coremail_user_infomation["coremail_user"],
                        org_unit_id=coremail_user_infomation["org_unit_id"],
                        password=coremail_user_infomation["password"],
                        user_status=coremail_user_infomation["user_status"],
                        cos_id=coremail_user_infomation["cos_id"],
                        quota_delta=coremail_user_infomation["quota_delta"],
                        true_name=coremail_user_infomation["coremail_user"])
    api_return_result = split_request_url.api_interface("createUser", create_user_attr)
    if api_return_result[0] == "0":
        print("Info: 创建用户 " + coremail_user_infomation["coremail_user"] + " 成功")
    else:
        print("\033[31;1mWarn:\033[0m 创建用户 " + coremail_user_infomation["coremail_user"] + " 失败:")
        print(api_return_result)

def get_deleteUser_Method(coremail_user_infomation):
    """
    :删除用户
    :param coremail_user_infomation: 用户信息字典
    :return:
    """
    delete_user_attr = "user_at_domain=%s@%s" % (
                        coremail_user_infomation["coremail_user"],
                        coremail_user_infomation["domain_name"])  # 删除的用户在"恢复已删除中"
    api_return_result = split_request_url.api_interface("deleteUser", delete_user_attr)
    if api_return_result[0] == "0":
        print("Info: 删除用户 " + coremail_user_infomation["coremail_user"] + " 成功")
    else:
        print("\033[31;1mWarn:\033[0m 删除用户 " + coremail_user_infomation["coremail_user"] + " 失败:")
        print(api_return_result)

def get_changeUser_Method(coremail_user_infomation):
    """
    :修改用户属性
    :param coremail_user_infomation: 用户信息字典
    :return:
    """
    change_user_attr = "user_at_domain={coremail_user}@{domain_name}&attrs=user_status%3D{user_status}" \
                       "%26user_list_rank%3D{user_list_rank}%26cos_id%3D{cos_id}%26password%3D{password}" \
                       "%26quota_delta%3D{quota_delta}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"],
        user_status=coremail_user_infomation["user_status"],
        user_list_rank=coremail_user_infomation["user_list_rank"],
        cos_id=coremail_user_infomation["cos_id"],
        quota_delta=coremail_user_infomation["quota_delta"],
        password=coremail_user_infomation["password"]
    )
    print("修改用户属性 " + coremail_user_infomation["coremail_user"])
    api_return_result = split_request_url.api_interface("changeAttrs", change_user_attr)
    if api_return_result[0] == "0":
        print("Info: 修改用户 " + coremail_user_infomation["coremail_user"] + " 成功")
    else:
        print("\033[31;1mWarn:\033[0m 修改用户 " + coremail_user_infomation["coremail_user"] + " 失败:")
        print(api_return_result)

def get_addSmtpAlias_Method(coremail_user_infomation):
    """
    :添加用户别名
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}&alias_user_at_domain={alias_user_at_domain}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"],
        alias_user_at_domain=coremail_user_infomation["alias_user_at_domain"]
    )
    api_return_result = split_request_url.api_interface("addSmtpAlias", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 用户 " + coremail_user_infomation["coremail_user"] + " 添加别名成功 " + coremail_user_infomation["alias_user_at_domain"])
    else:
        print("\033[31;1mWarn:\033[0m 用户 " + coremail_user_infomation["coremail_user"] + " 添加别名失败 " + coremail_user_infomation["alias_user_at_domain"])
        print(api_return_result)

def get_getSmtpAlias_Method(coremail_user_infomation):
    """
    :列出用户别名
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"]
    )
    api_return_result = split_request_url.api_interface("getSmtpAlias", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 用户 " + coremail_user_infomation["coremail_user"] + " 的别名: " + api_return_result[1])
    else:
        print("\033[31;1mWarn:\033[0m 获取用户 " + coremail_user_infomation["coremail_user"] + " 别名出错:")
        print(api_return_result)

def get_delSmtpAlias_Method(coremail_user_infomation):
    """
    :删除用户别名
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}&alias_user_at_domain={alias_user_at_domain}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"],
        alias_user_at_domain=coremail_user_infomation["alias_user_at_domain"])
    api_return_result = split_request_url.api_interface("delSmtpAlias", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 删除用户 " + coremail_user_infomation["coremail_user"] + " 的别名成功")
    else:
        print("\033[31;1mWarn:\033[0m 删除用户 " + coremail_user_infomation["coremail_user"] + " 别名出错:")
        print(api_return_result)

def get_setAdminType_Method(coremail_user_infomation):
    """
    :将用户设置为组织管理员
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"]
    )
    api_return_result = split_request_url.api_interface("setAdminType", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 已将用户 " + coremail_user_infomation["coremail_user"] + " 设置为组织管理员")
    else:
        print("\033[31;1mWarn:\033[0m 用户 " + coremail_user_infomation["coremail_user"] + " 设置组织管理员出错:")
        print(api_return_result)

def get_renameUser_Method(coremail_user_infomation):
    """
    :修改邮箱地址前缀
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}&new_user_id={new_user_id}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"],
        new_user_id=coremail_user_infomation["new_user_id"]
    )
    api_return_result = split_request_url.api_interface("renameUser", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 已将用户 " + coremail_user_infomation["coremail_user"] + " 的前缀修改为 " + coremail_user_infomation["new_user_id"])
    else:
        print("\033[31;1mWarn:\033[0m 修改用户 " + coremail_user_infomation["coremail_user"] + " 前缀出错:")
        print(api_return_result)

def get_moveUser_Method(coremail_user_infomation):
    """
    :跨组织移动用户 默认移动到根目录下，可移动到某个部门下，需要自定部门 org_unit_id
    :param coremail_user_infomation:
    :return:
    """
    coremail_user_attr = "user_at_domain={coremail_user}@{domain_name}&attrs=org_id%3D{new_org_id}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"],
        new_org_id=coremail_user_infomation["new_org_id"]
    )
    api_return_result = split_request_url.api_interface("moveUser", coremail_user_attr)
    if api_return_result[0] == "0":
        print("Info: 已成功将用户 " + coremail_user_infomation["coremail_user"] + " 移动到新组织中 " + coremail_user_infomation["new_org_id"])
    else:
        print("\033[31;1mWarn:\033[0m 移动用户 " + coremail_user_infomation["coremail_user"] + " 到新组织出错: ")
        print(api_return_result)






















