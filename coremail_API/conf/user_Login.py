from conf import split_request_url
import webbrowser
import time

def user_Login_Method(coremail_user_infomation):
    """
    :用户单点登陆
    :param coremail_user_infomation:
    :return:
    """
    user_login_attr = "user_at_domain={coremail_user}@{domain_name}".format(
        coremail_user=coremail_user_infomation["coremail_user"],
        domain_name=coremail_user_infomation["domain_name"]
    )
    api_return_result = split_request_url.api_interface("userLogin", user_login_attr)
    if api_return_result[0] == "0":
        fid = "\"fid\""
        common_user = "http://192.168.213.186:9900/coremail/main.jsp?sid=" + api_return_result[1]
        print("普通用户单点登陆")
        print(common_user)
        webbrowser.open(common_user, autoraise=True)  # 自动打开浏览器并输入url登陆
    else:
        print("\033[31;1mWarn:\033[0m 单点失败")
        print(api_return_result)

    # 检查用户的session 并返回用户信息
    coremail_user_session_info = "ses_id=%s" % api_return_result[1]
    api_return_user_session = split_request_url.api_interface("sesTimeOut", coremail_user_session_info)
    if api_return_user_session[0] == "0":
        print("Info: 读取session id返回用户信息: " + api_return_user_session[1])
    else:
        print("\033[31;1mWarn:\033[0m 用户的session出错:")
        print(api_return_user_session)

    # # 检查用户的session, 并刷新访问时间
    # # time.sleep(5)
    # api_return_user_session = split_request_url.api_interface("sesRefresh", coremail_user_session_info)
    # if api_return_user_session[0] == "0":
    #     print("Info: 刷新session的访问时间: " + api_return_user_session[1])
    #     print("Info: 好像什么都没输出哦")
    # else:
    #     print("\033[31;1mWarn:\033[0m 刷新session的访问时间出错:")
    #     print(api_return_user_session)

    # # 获取session中的变量
    # coremail_user_sessionVar = "ses_id=%s&ses_key" % api_return_result[1]
    # api_return_user_session = split_request_url.api_interface("getSessionVar", coremail_user_sessionVar)
    # if api_return_user_session[0] == "0":
    #     print("Info: 获取session中的变量: " + api_return_user_session[1])
    #     print("Info: 好像什么都没输出哦")
    # else:
    #     print("\033[31;1mWarn:\033[0m 获取session中的变量出错:")
    #     print(api_return_user_session)



def admin_login():
    # 单点登陆  管理员登陆
    admin_user_login_attr = "user_at_domain=admin@leejay.vip"
    api_returnAdmin_result = split_request_url.api_interface("userLogin", admin_user_login_attr)
    print("管理员单点登陆url：")
    if api_returnAdmin_result[0] == "0":
        admin_user = "http://192.168.213.186:9900/webadmin/~{sid}/~/usr/index_usr.jsp".format(sid=api_returnAdmin_result[1])
        print(admin_user)
    else:
        print("获取管理员 session id 失败:")
        print(api_returnAdmin_result)
    webbrowser.open_new_tab(admin_user)




