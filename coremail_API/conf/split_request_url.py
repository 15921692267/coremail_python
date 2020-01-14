import requests
import re

def get_token():
    # 授权apiacl的邮箱用户
    mail_apiacl_user = "leejay"
    user_passwd = "1"

    # 获取token
    GET_USERINFO_URL = "http://192.168.213.186:9900/apiws/services/API2/requestToken?app_id={user_id}&secret={passwd}"
    token_url_address = GET_USERINFO_URL.format(user_id=mail_apiacl_user, passwd=user_passwd)
    token_space_list = list(request_split(token_url_address))  # 将url传给request_split()函数进行请求,接收的是一个元组转成列表方便修改
    # print(token_space_list)
    token_list = token_space_list[1].split()  # token中带有空格，需分隔后进行拼接 获取的是sid 和 token
    if token_space_list[0] == "0":
        token = token_list[0] + "+" + token_list[1]  # 拼接sid+token
        # print("Info: 获取token和session id成功 " + token)
    else:
        print("\033[31;1mWarn:\033[0m 获取token失败")
        print(token_list[0])
    return token

def api_interface(get_method, attrs_name, *args):
    """
    :param attrs:  请求的属性
    :param attrs_name:  属性名
    :return:
    """
    token = get_token()  # 获得token的值
    # 通过token访问API
    api_interface = "http://192.168.213.186:9900/apiws/services/API2/{get_method}?_token={_token}&{attrs_name}"
    api_interface_format_url = api_interface.format(get_method=get_method, _token=token, attrs_name=attrs_name)  # 格式化api_interface
    print("Info: 拼接后链接，用于请求coremailAPI")
    print(api_interface_format_url)
    get_api_return_result = request_split(api_interface_format_url)  # 调用函数请求url，得到邮箱系统返回的结果
    return get_api_return_result

def request_split(request_url):
    """
    :param request_url:  需要request的url
    :return: 邮箱系统反馈的结果
    """
    user_info = requests.get(request_url)  # 获取传来的url
    # print(user_info.text)
    re_split_list = re.split('[<>]', user_info.text)  # 按照'<>'分隔为列表
    # print(re_split_list)
    api_return_code = re_split_list[10]  # 获取返回码
    api_return_result = re_split_list[14]   # 提取第14位，即调用邮箱系统的API返回的结果

    return api_return_code, api_return_result  # 调用方接收的会是一个元组