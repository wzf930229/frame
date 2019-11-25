from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_currency(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_currency.json"
        self.f2="data_currency.xls"
    def write2excel(self,r,col,f):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], 200)
        writeResult(col, self.r_col, "pass",f)
        writeResult(col, self.t_col, r.elapsed.total_seconds(),f)
    def tearDown(self):
        pass

    # 登陆接口
    def test_001(self):
        r = self.obj.post(1, self.f, self.f2)
        writeToken(r.json()["data"]["token"])
        # r=self.obj.post_token(2)
        self.write2excel(r, 1, self.f2)
    def test_002(self):
        #企业货币列表（分页）
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #新增币种
        r=self.obj.post_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        #根据ID查询币种信息
        id=r.json()["data"]["id"]
        r=self.obj.get_v(4,id,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #编辑币种
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #分页查询货币汇率信息
        r=self.obj.get_t(6,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #新增企业货币汇率
        r=self.obj.post_t(7,self.f1,self.f2)
        self.write2excel(r,7,self.f2)
        #编辑企业货币汇率
        id1=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id1)
        r=self.obj.post_c(8,self.f1,self.f2,l,li)
        self.write2excel(r,8,self.f2)
        #删除企业货币汇率
        l=[]
        li=[]
        l.append("ids")
        li.append([id1])
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #删除企业货币
        r=self.obj.get_v(10,id,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
    def test_003(self):
        #获取可用货币列表
        r=self.obj.get_t(11,self.f1,self.f2)
        print(r.text)
        self.write2excel(r,11,self.f2)
if __name__ == '__main__':
    unittest.main()