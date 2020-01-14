from conf import user_operate_method
from conf import user_Login
import urllib



coremail_user_infomation = {
    "coremail_user": "coremail_0007",
    "password": "1",
    "user_status": "0",
    "cos_id": "1",   # 服务等级
    "quota_delta": "0",   # 邮箱容量
    "user_list_rank": "100",  # 排序
    "alias_user_at_domain": "cmail005d@leejay.vip",
    "domain_name": "leejay.vip",
    "new_user_id": "cm_006",  # 新前缀，修改邮箱地址前缀会用到
    "org_id": "a",
    "provider_id": "1",
    "org_unit_id": "20200112",  # 创建用户会用到，将用户创建到哪个部门里，空代表根目录
    "new_org_id": "atnc.com.cn",  # 跨组织移动会用到
    "new_org_unit_id": ""   # 新部门标识符，跨组织移动会用到
}

# 用户单点登陆  检查用户session
# user_Login.user_Login_Method(coremail_user_infomation)

# 管理员单点登陆
# user_Login.admin_login()

# 获取用户信息 获取未读邮件数等
# user_operate_method.getAttrs_Method(coremail_user_infomation)

# 获取用户未读邮件列表
# user_operate_method.getNewMailInfos_Method(coremail_user_infomation)

# 删除邮件  删不掉  调用不到API
# user_operate_method.get_deleteMailInfos_Method(coremail_user_infomation)

# 检测用户是否存在
# user_operate_method.get_userExist_Method(coremail_user_infomation)

# 创建用户
# user_operate_method.get_createUser_Method(coremail_user_infomation)

# 循环创建用户  超出license个数会报('59', 'user license exceed')
# for i in range(9999):
#     coremail_user_infomation["coremail_user"] = "coremail_" + str(i)
#     user_operate_method.get_createUser_Method(coremail_user_infomation)


# 删除用户
# user_operate_method.get_deleteUser_Method(coremail_user_infomation)

# 修改用户
# user_operate_method.get_changeUser_Method(coremail_user_infomation)

# 添加别名  要添加邮箱系统上已存在的域名，否则会报"Domain not found:qq.com"
# user_operate_method.get_addSmtpAlias_Method(coremail_user_infomation)

# 获取用户别名
# user_operate_method.get_getSmtpAlias_Method(coremail_user_infomation)

# 删除用户别名
# user_operate_method.get_delSmtpAlias_Method(coremail_user_infomation)

# 将用户设置为管理员 组织管理员 用户在"恢复已删除"中也可以设置成功
# user_operate_method.get_setAdminType_Method(coremail_user_infomation)

# 修改邮箱地址前缀
# user_operate_method.get_renameUser_Method(coremail_user_infomation)

# 用户跨组织移动 将XXX@leejay.vip移动到组织atnc.com.cn下，需要将leejay.vip添加到组织atnc.com.cn中的域名中
# user_operate_method.get_moveUser_Method(coremail_user_infomation)





