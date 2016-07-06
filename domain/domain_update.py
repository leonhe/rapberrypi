#!/usr/bin/python
#-*-coding:utf-8 --
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainInfoRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest
import json
import urlparse
import re,urllib2
from subprocess import Popen, PIPE
UPDATE_DOMAIN="你的域名"#如：feiio.com
AccessKey = ""
AcessSecret=""
#万网网页获取IP地址
page_value=urllib2.urlopen("http://www.net.cn/static/customercare/yourip.asp").read()
waln_ip=re.search('\d+\.\d+\.\d+\.\d+',page_value).group(0) #waln ip

clt = client.AcsClient(AccessKey,AccessSecret,"cn-hangzhou")
def updateDomain(rid,rp,types,value):
    update_domain_request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    update_domain_request.set_RecordId(rid)
    update_domain_request.set_RR(rp)
    update_domain_request.set_Type(types)
    update_domain_request.set_Value(value)
    update_domain_request.set_accept_format('json')
    return clt.do_action(update_domain_request)
#Rcords Domain
domain_records = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
domain_records.set_DomainName(Domain)
domain_records.set_accept_format('json')
result = clt.do_action(domain_records)
data = json.loads(result)
count=data["TotalCount"]
record=data["DomainRecords"]["Record"]
for index in range(count):
    line_value=record[index]
    if line_value["Type"]=="A" and line_value["Value"]!=waln_ip:
        result=updateDomain(line_value["RecordId"],line_value["RR"],line_value["Type"],waln_ip)
        print("更新IP to:"+waln_ip)
print("excute domain ip update check!!!")
