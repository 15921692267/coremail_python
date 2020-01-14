from conf import org_Operate_Method

coremail_org_information = {
    "org_id": "a",
    "org_name": "qq组织",  # 组织的名字  创建组织或修改组织用到
    "domain_name": "qq.com.cn",  # 组织使用的域名
    "res_grp_id": "0",    # 资源分组为0  programs/RmiServer/APIDefaultRes下的配置值
    "cos_id": "1",  # 服务等级ID, 1 代表缺省服务  programs/RmiServer/APIDefaultCos下的配置值（配置值用cos_name指定COS）
    "num_of_classes": "123",  # COS ID类型 用户数限制 123个
    "org_status": "0",  # 企业状态（0正常1暂停2锁定）
    "org_expiry_date": "",   # 过期日期。NULL或者空表示不过期。 格式为: yyyy-MM-dd
    "org_options": "3",    # 组织增值服务开关 0-全关闭  1-开通组织通讯录  2-开通企业公告  3-同时开通全面两项服务
    "org_assignable_quota": "125",   # 邮箱附加容量 125M
    "domain_name_alias": "leejay.com.cn",   # 域别名
    "new_domain_name": "qq.com",
    "parent_org_unit_id": "",    # 父部门 创建部门的时候,如果为空,会在根目录下创建
    "org_unit_id": "20200112",
    "org_unit_name": "茶叶镇",
    "change_org_unit_name": "阿里部"
}

# 增加组织
# org_Operate_Method.get_addOrg_Method(coremail_org_information)

# 获取组织信息
# org_Operate_Method.getOrgInformation_Method(coremail_org_information)

# 修改组织属性
# org_Operate_Method.get_alterOrg_Method(coremail_org_information)

# 组织增加新域名
# org_Operate_Method.get_addOrgDomain_Method(coremail_org_information)

# 组织删除新域名
# org_Operate_Method.get_delOrgDomain_Method(coremail_org_information)

# 判断域名或域别名是否存在  返回码为 0 表示存在
# org_Operate_Method.get_domainExist_Method(coremail_org_information)

# 列出系统所有的域名
# org_Operate_Method.getDomainList_Method()

# 增加域名
# org_Operate_Method.get_addDomain25_Method(coremail_org_information)

# 删除域名
# org_Operate_Method.get_delDomain25_Method(coremail_org_information)

# 增加域别名
# org_Operate_Method.get_addDomainAlias_Method(coremail_org_information)

# 删除域别名
# org_Operate_Method.get_delDomainAlias_Method(coremail_org_information)

# 创建部门
# org_Operate_Method.get_addUnit_Method(coremail_org_information)

# 删除部门
# org_Operate_Method.get_delUnit_Method(coremail_org_information)

# 获取部门属性
# org_Operate_Method.getUnitAttrs_Method(coremail_org_information)

# 设置部门属性
# org_Operate_Method.get_setUnitAttrs_Method(coremail_org_information)




