#!/usr/bin/python
# -*- coding: utf-8 -*- 
import dns.resolver
import sys
import os
def dns_query(domain, type):
    """
    MX、A、TXT记录查询    
    :param domain: 传过来的域名
    :param type: 类型为 MX A TXT
    :return:
    """
    print("\033[31;1m%s记录：\033[0m" % type)
    try:
        dnsquery = dns.resolver.query(domain, type)
        mx_record = []
        for i in dnsquery.response.answer:
            for j in i:
                print("---> %s" % j)
                mx_record.append(j)
    except dns.resolver.NoAnswer:
        print(domain+' DNS未响应！')
        exit()
    return mx_record

def nmap_ip_port(nmap_ip_list):
    """
    查询ip的端口号    
    :param nmap_ip_list: A记录中查询的IP列表
    :return:
    """
    nmap_ip_list_unrepeat = []
    for ip_line in nmap_ip_list:
        if ip_line not in nmap_ip_list_unrepeat:
            nmap_ip_list_unrepeat.append(ip_line)
    for ip_line_2 in nmap_ip_list_unrepeat:
        print "-----------"
        print "\033[32;1m%s\033[0m" % ip_line_2
        os.system("nmap -Pn %s" % ip_line_2)


def main():
    try:
        print "eg: ./dns_resolve_def.py coremail.cn"
        domain = sys.argv[1]
        receive_mx = dns_query(domain, 'MX')
        dns_query(domain, 'TXT')
        print "+++++++++++"
        nmap_ip_list = []
        for mx_index in range(len(receive_mx)):
            # print receive_mx[mx_index]
            mx_record = str(receive_mx[mx_index]).split()
            print "----------"
            print mx_record[1]
            ip_List = dns_query(mx_record[1], 'A')
            for ip_line in range(len(ip_List)):
                nmap_ip_list.append(ip_List[ip_line])
        print "++++++++++++"
        print "Info: view nmap ip"
        nmap_ip_port(nmap_ip_list)
    except Exception as e:
        print e




if __name__ == "__main__":
    main()
