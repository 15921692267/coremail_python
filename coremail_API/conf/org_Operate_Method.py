from conf import split_request_url
import re
"""
attrs=后面的等号和&号都要用下面的字符 attrs 参数传递，并且 attrs 参数中的 = 和 & 要转成 url 编码
= 对应 %3D
& 对应 %26
api_interface() # 调用这个函数返回一个元组：一个返回码 一个api调用返回的结果
"""

def get_addOrg_Method(coremail_org_information):
    """
    :增加组织
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&attrs=org_name%3D{org_name}%26domain_name%3D{domain_name}%26" \
                "res_grp_id%3D{res_grp_id}%26cos_id%3D{cos_id}%26num_of_classes%3D{num_of_classes}%26" \
                "org_assignable_quota%3D{org_assignable_quota}%26org_status%3D{org_status}" \
                "%26org_expiry_date%3D{org_expiry_date}%26org_options%3D{org_options}".format(
        org_id=coremail_org_information["org_id"],
        org_name=coremail_org_information["org_name"],
        domain_name=coremail_org_information["domain_name"],
        res_grp_id=coremail_org_information["res_grp_id"],
        cos_id=coremail_org_information["cos_id"],
        num_of_classes=coremail_org_information["num_of_classes"],
        org_assignable_quota=coremail_org_information["org_assignable_quota"],
        org_status=coremail_org_information["org_status"],
        org_expiry_date=coremail_org_information["org_expiry_date"],
        org_options=coremail_org_information["org_options"]
    )
    api_return_result = split_request_url.api_interface("addOrg", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 组织添加成功: " + coremail_org_information["org_id"] + " " + coremail_org_information["org_name"])
    else:
        print("\033[31;1mWarn:\033[0m 添加组织失败")
        print(api_return_result)

def getOrgInformation_Method(coremail_org_information):
    """
    :获取组织的信息
    :param coremail_user_infomation:
    :return:
    """
    org_attrs = "org_id={org_id}&attrs=org_name%26provider_id%26org_id%26org_assignable_quota%26" \
                "org_status%26org_creation_date%26org_expiry_date%26org_xbcc%26org_list_rank%26org_nf_quota_delta%26" \
                "org_admin_ip_limit%26org_access_level%26org_region_id%26email_allow_user%26domain_name" \
                "%26not_used_quota".format(
        org_id=coremail_org_information["org_id"],

    )
    api_return_result = list(split_request_url.api_interface("getOrgInfo", org_attrs))  # 传入方法 和 方法中的属性
    org_result_list = re.split("&amp;", api_return_result[1])
    if api_return_result[0] == "0":
        print("Info: 获取组织信息成功")
        for org_info in org_result_list:
            print(org_info)
    else:
        print("\033[31;1mWarn:\033[0m 返回组织 " + coremail_org_information["org_id"] + " 信息失败：")
        print(api_return_result)

def get_alterOrg_Method(coremail_org_information):
    """
    :修改组织属性
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&attrs=org_name%3D{org_name}%26" \
                "res_grp_id%3D{res_grp_id}%26org_assignable_quota%3D{org_assignable_quota}" \
                "%26org_status%3D{org_status}%26org_expiry_date%3D{org_expiry_date}%26".format(
        org_id=coremail_org_information["org_id"],
        org_name=coremail_org_information["org_name"],
        # domain_name=coremail_org_information["domain_name"],  # 加上这个报错
        res_grp_id=coremail_org_information["res_grp_id"],
        org_assignable_quota=coremail_org_information["org_assignable_quota"],
        org_status=coremail_org_information["org_status"],
        org_expiry_date=coremail_org_information["org_expiry_date"]
    )
    api_return_result = split_request_url.api_interface("alterOrg", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 组织属性修改成功: " + coremail_org_information["org_id"] + " " + coremail_org_information["org_name"])
    else:
        print("\033[31;1mWarn:\033[0m 组织属性修改失败")
        print(api_return_result)

def get_addOrgDomain_Method(coremail_org_information):
    """
    :组织增加新域名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&domain_name={new_domain_name}".format(
        org_id=coremail_org_information["org_id"],
        new_domain_name=coremail_org_information["new_domain_name"]
    )
    api_return_result = split_request_url.api_interface("addOrgDomain", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 组织增加新域名成功: " + coremail_org_information["org_id"] + " " + coremail_org_information["new_domain_name"])
    else:
        print("\033[31;1mWarn:\033[0m 组织增加新域名失败:")
        print(api_return_result)

def get_delOrgDomain_Method(coremail_org_information):
    """
    :删除组织新加的域名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&domain_name={new_domain_name}".format(
        org_id=coremail_org_information["org_id"],
        new_domain_name=coremail_org_information["new_domain_name"]
    )
    api_return_result = split_request_url.api_interface("delOrgDomain", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 组织新域名删除成功: " + coremail_org_information["org_id"] + " " + coremail_org_information["new_domain_name"])
    else:
        print("\033[31;1mWarn:\033[0m 组织新域名删除失败")
        print(api_return_result)


def get_domainExist_Method(coremail_org_information):
    """
    :判断域名或者域别名是否存在
    :param coremail_org_information:
    :return:
    """
    org_attrs = "domain_name={domain_name}".format(
        domain_name=coremail_org_information["domain_name"]
    )
    api_return_result = split_request_url.api_interface("domainExist", org_attrs)  # 接收的是一个元组：一个返回码 一个api调用返回的结果
    if api_return_result[0] == "0":
        print("Info: 域名 " + api_return_result[1] + " 存在，返回码：" + api_return_result[0])
    else:
        print("\033[31;1mWarn:\033[0m 域名不存在 ")
        print(api_return_result)

def getDomainList_Method():
    """
    :列出系统所有的域名
    :param coremail_org_information:
    :return:
    """
    org_attrs = ""
    print(split_request_url.api_interface("getDomainList", org_attrs))

def get_addDomain25_Method(coremail_org_information):
    """
    :增加一个新域名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "domain_name={new_domain_name}".format(
        new_domain_name=coremail_org_information["new_domain_name"]
    )
    api_return_result = split_request_url.api_interface("addDomain25", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 域名 " + coremail_org_information["new_domain_name"] + " 添加成功")
    else:
        print("\033[31;1mWarn:\033[0m 域名 " + coremail_org_information["new_domain_name"] + "添加失败：")
        print(api_return_result)

def get_delDomain25_Method(coremail_org_information):
    """
    :删除一个域名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "domain_name={new_domain_name}".format(
        new_domain_name=coremail_org_information["new_domain_name"]
    )
    api_return_result = split_request_url.api_interface("delDomain25", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 域名 " + coremail_org_information["new_domain_name"] + " 删除成功")
    else:
        print("\033[31;1mWarn:\033[0m 域名 " + coremail_org_information["new_domain_name"] + " 删除失败：")
        print(api_return_result)

def get_addDomainAlias_Method(coremail_org_information):
    """
    :增加域别名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "domain_name={domain_name}&domain_name_alias={domain_name_alias}".format(
        domain_name=coremail_org_information["domain_name"],
        domain_name_alias=coremail_org_information["domain_name_alias"]
    )
    api_return_result = split_request_url.api_interface("addDomainAlias", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 域别名 " + coremail_org_information["domain_name_alias"] + " 增加成功")
    else:
        print("\033[31;1mWarn:\033[0m 域别名 " + coremail_org_information["domain_name_alias"] + " 增加失败：")
        print(api_return_result)

def get_delDomainAlias_Method(coremail_org_information):
    """
    :删除域别名
    :param coremail_org_information:
    :return:
    """
    org_attrs = "domain_name={domain_name}&domain_name_alias={domain_name_alias}".format(
        domain_name=coremail_org_information["domain_name"],
        domain_name_alias=coremail_org_information["domain_name_alias"]
    )
    api_return_result = split_request_url.api_interface("delDomainAlias", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 域别名 " + coremail_org_information["domain_name_alias"] + " 删除成功")
    else:
        print("\033[31;1mWarn:\033[0m 域别名 " + coremail_org_information["domain_name_alias"] + " 删除失败：")
        print(api_return_result)

def get_addUnit_Method(coremail_org_information):
    """
    :增加部门
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&org_unit_id={org_unit_id}&attrs=parent_org_unit_id%3D{parent_org_unit_id}%26org_unit_name%3D{org_unit_name}".format(
            org_id=coremail_org_information["org_id"],
            org_unit_id=coremail_org_information["org_unit_id"],
            org_unit_name=coremail_org_information["org_unit_name"],
            parent_org_unit_id=coremail_org_information["parent_org_unit_id"]
    )
    api_return_result = split_request_url.api_interface("addUnit", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 增加部门成功\t" + coremail_org_information["org_unit_id"] + "\t" + coremail_org_information["org_unit_name"])
    else:
        print("\033[31;1mWarn:\033[0m 增加部门失败")
        print(api_return_result)

def get_delUnit_Method(coremail_org_information):
    """
    :删除部门
    :param coremail_org_information:
    :return:
    """
    org_attrs = "org_id={org_id}&org_unit_id={org_unit_id}".format(
            org_id=coremail_org_information["org_id"],
            org_unit_id=coremail_org_information["org_unit_id"]
    )
    api_return_result = split_request_url.api_interface("delUnit", org_attrs)
    if api_return_result[0] == "0":
        print("Info: 删除部门成功\t" + coremail_org_information["org_unit_id"])
    else:
        print("\033[31;1mWarn:\033[0m 删除部门失败")
        print(api_return_result)

def getUnitAttrs_Method(coremail_org_information):
    """
    :获取部门信息
    :param coremail_org_information:
    :return:
    """
    unit_attrs = "org_id={org_id}&org_unit_id={org_unit_id}&attrs=parent_org_unit_id%26org_unit_name".format(
        org_id=coremail_org_information["org_id"],
        org_unit_id=coremail_org_information["org_unit_id"]
    )
    api_return_result = split_request_url.api_interface("getUnitAttrs", unit_attrs)
    if api_return_result[0] == "0":
        print("Info: 成功获取到部门信息\t" + api_return_result[1])
    else:
        print("\033[31;1mWarn:\033[0m 获取部门信息失败")
        print(api_return_result)

def get_setUnitAttrs_Method(coremail_org_information):
    """
    :修改部门属性
    :param coremail_org_information:
    :return:
    """
    unit_attrs = "org_id={org_id}&org_unit_id={org_unit_id}&attrs=org_unit_name%3D{change_org_unit_name}".format(
        org_id=coremail_org_information["org_id"],
        org_unit_id=coremail_org_information["org_unit_id"],
        change_org_unit_name=coremail_org_information["change_org_unit_name"]
    )
    api_return_result = split_request_url.api_interface("setUnitAttrs", unit_attrs)
    if api_return_result[0] == "0":
        print("Info: 已成功将部门id为 " + coremail_org_information["org_unit_id"] + " 的名字改为 " + coremail_org_information["change_org_unit_name"])
    else:
        print("\033[31;1mWarn:\033[0m 设置部门属性失败")
        print(api_return_result)