from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_busi(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f1="requestData_busi.json"
        self.f2="data_busi.xls"
        self.f="public_url.json"
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
        #获取物业列表
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        id=r.json()["data"]["rows"][0]["id"]
        #获取物业详情
        r=self.obj.get_v(3,id,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        shopId=r.json()["data"]["rows"][0]["shopId"]
        #编辑保存物业信息
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #获取物业下的收入中心列表
        l=[]
        li=[]
        l.append("shopId")
        li.append(shopId)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #获取当前企业下物业收入中心树
        r=self.obj.get_t(6,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #通过物业信息查询物业所绑定的维度信息
        l=[]
        li=[]
        l.append("entityId")
        li.append(id)
        r=self.obj.get_c(7,self.f1,self.f2,l,li)
        self.write2excel(r,7,self.f2)
        #获取物业所属企业层级
        r=self.obj.get_v(9,id,self.f1,self.f2)
        self.write2excel(r,9,self.f2)
    def test_003(self):
        #物业&收入中心绑定维度标签
        r=self.obj.post_t(8,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
if __name__ == '__main__':
    unittest.main()