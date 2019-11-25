from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_tenant(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_tenant.json"
        self.f2="data_tenant.xls"
    def write2excel(self,r,col,f):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], 200)
        writeResult(col, self.r_col, "pass",f)
        writeResult(col, self.t_col, r.elapsed.total_seconds(),f)
    def tearDown(self):
        pass

    # 登陆接口
    def test_001(self):
        r = self.obj.post(1,self.f,self.f2)
        writeToken(r.json()["data"]["token"])
        # r=self.obj.post_token(2)
        self.write2excel(r, 1,self.f2)
    def test_002(self):
        #企业信息查询
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
    def test_003(self):
        #企业密码策略查询
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
    def test_004(self):
        #企业信息编辑保存
        r=self.obj.post_t(4,self.f1,self.f2)
        print(r.text)
        self.write2excel(r,4,self.f2)
if __name__ == '__main__':
    unittest.main()