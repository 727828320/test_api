import json

import pytest

from common.login import company_login_token
from utils.operationExcel import ExcelVarles, OperationExcel
from base.method import ApiRequest as obj
# [
#     {'用例ID': 1.0, '用例模块': '部门', '用例名称': '创建部门', '请求地址': 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
#      '请求方式': 'post', '请求类型': 'json',
#      '请求参数': {"name": "广州研发中心","name_en": "RDGZ","parentid": 1,"order": 1,"id": 2},
#      '请求头': '', '状态码': 0.0, '预期结果': '{\n   "errcode": 0,\n   "errmsg": "created",\n   "id": 2\n}', '是否执行？': ''}]

@pytest.mark.parametrize('data', OperationExcel().getExceldatas())
def test_api_all(data, company_login_token):
    if data[ExcelVarles.case_method] == 'get':
        r = obj().send_requests(method='get', url=data[ExcelVarles.case_url])
    elif data[ExcelVarles.case_method] == 'post':
        print(data[ExcelVarles.case_url] + "?access_token=" + company_login_token)
        r = obj().send_requests(method='post', url=data[ExcelVarles.case_url] + "?access_token=" + company_login_token,
                                data=data[ExcelVarles.case_data])
        print(r)
