import xlrd
from common.public import filePath


class OperationExcel:
    def getSheet(self):
        book = xlrd.open_workbook(filePath())
        return book.sheet_by_index(0)

    def getExceldatas(self):
        data = []
        title = self.getSheet().row_values(0)
        for i in range(1, self.getSheet().nrows):
            row_value = self.getSheet().row_values(i)
            data.append(dict(zip(title, row_value)))
        return data

class ExcelVarles:
    case_ID = '用例ID'
    case_module = '用例模块'
    case_name = '用例名称'
    case_url = '请求地址'
    case_method = '请求方式'
    case_type = '请求类型'
    case_data = '请求参数'
    case_headers = '请求头'
    case_code = '状态码'
    case_result = '预期结果'
