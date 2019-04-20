#!/usr/bin/env python
# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('AccessKeyId', 'AccessKeySecret', 'default')  # 创建Client实例

request = CommonRequest()  # 创建API请求request并设置参数。
request.set_accept_format('json')  # 设置返回数据格式，默认为XML
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https')  # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('SignName', '美世教育')
request.add_query_param('TemplateCode', 'SMS_163852162')
request.add_query_param('PhoneNumbers', '15850783283')
request.add_query_param('TemplateParam', '{"code":"123456"}')

response = client.do_action_with_exception(request)  # 用client身份去执行request请求，发起API请求并显示返回值
print(str(response, encoding='utf-8'))
