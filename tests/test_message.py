#作者:Administrator
#时间:2019/10/20
from base.method import *
from utils.excel_data import excel_data as e
import unittest
from page.openS import *
class test_message(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data=e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_message.json"
        self.f2="data_message.xls"

    def write2excel(self,r,col,f):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], 200)
        writeResult(col, self.r_col, "pass",f)
        writeResult(col, self.t_col, r.elapsed.total_seconds(),f)
    def tearDown(self):
        pass
    #登陆接口
    def test_001(self):
        r=self.obj.post(1,self.f,self.f2)
        writeToken(r.json()["data"]["token"])
        #r=self.obj.post_token(2)
        self.write2excel(r,1,self.f2)
    #忘记密码
    def test_002(self):
        r=self.obj.get(2,self.f1,self.f2)
        print(r.text)
        self.write2excel(r, 2,self.f2)
    #获取个人信息
    def test_003(self):
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r, 3,self.f2)
    #保存个人信息
    def test_004(self):
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r, 4,self.f2)
    #获取收到消息列表
    def test_005(self):
        r=self.obj.post_t(5,self.f1,self.f2)
        self.write2excel(r, 5,self.f2)
    #获取已发送消息列表
    def test_006(self):
        r=self.obj.post_t(6,self.f1,self.f2)
        self.write2excel(r, 6,self.f2)
        total=r.json()["data"]["total"]
        if total!=0:
            id=r.json()["data"]["rows"][0]["id"]
            # 获取单条消息详情
            rt=self.obj.get_v(7,id,self.f1,self.f2)
            self.write2excel(rt, 7,self.f2)
    #标记消息
    def test_008(self):
        r = self.obj.post_t(5,self.f1,self.f2)
        total = r.json()["data"]["total"]
        if total!=0:
            id = r.json()["data"]["rows"][0]["id"]
            #标记消息
            r= self.obj.get_v(8, id,self.f1,self.f2)
            self.write2excel(r, 8,self.f2)
            #取消标记
            r=self.obj.get_v(9,id,self.f1,self.f2)
            self.write2excel(r, 9,self.f2)
            #标识重要
            r = self.obj.get_v(10, id,self.f1,self.f2)
            self.write2excel(r, 10,self.f2)
            #取消重要
            r = self.obj.get_v(11, id,self.f1,self.f2)
            print(r.text)
            self.write2excel(r, 11,self.f2)
    #新增消息
    def test_012(self):
        r=self.obj.post_t(12,self.f1,self.f2)
        self.write2excel(r,12,self.f2)
    #查询用户未读摘要消息
    def test_013(self):
        r=self.obj.get_t(13,self.f1,self.f2)
        self.write2excel(r,13,self.f2)
    #获取登陆用户的消息收件人列表
    def test_014(self):
        r=self.obj.get_t(14,self.f1,self.f2)
        self.write2excel(r, 14,self.f2)

if __name__ == '__main__':
    unittest.main()

