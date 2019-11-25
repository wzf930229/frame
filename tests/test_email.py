from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_email(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_email.json"
        self.f2="data_email.xls"
    def write2excel(self,r,col,f):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], 200)
        writeResult(col, self.r_col, "pass",f)
        writeResult(col, self.t_col, r.elapsed.total_seconds(),f )
    def tearDown(self):
        pass
    def test_001(self):
        #登陆系统
        r=self.obj.post(1,self.f,self.f2)
        writeToken(r.json()["data"]["token"])
        #r=self.obj.post_token(2)
        self.write2excel(r,1,self.f2)
    def test_002(self):
        #获取企业邮件模板列表
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #获取企业邮件模板（获取单个模板）
        id=r.json()["data"]["rows"][0]["id"]
        r=self.obj.get_v(3,id,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
    def test_003(self):
        #新增企业邮件模板
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #编辑企业邮件模板
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #禁用企业邮件模板
        r=self.obj.get_v(6,id,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #启用企业邮件模板
        r=self.obj.get_v(7,id,self.f1,self.f2)
        self.write2excel(r,7,self.f2)
        #删除企业邮件模板
        r=self.obj.get_v(8,id,self.f1,self.f2)
        self.write2excel(r,8,self.f2)

if __name__ == '__main__':
    unittest.main