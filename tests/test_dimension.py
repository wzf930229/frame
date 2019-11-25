from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_dimension(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_dimension.json"
        self.f2="data_dimension.xls"
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
        #获取物业维度列表
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        # 维度值列表
        id=r.json()["data"][0]["id"]
        l = []
        li = []
        l.append("dimensionTypeId")
        li.append(id)
        r = self.obj.get_c(10, self.f1, self.f2, l, li)
        self.write2excel(r, 10, self.f2)
        #维度值下移
        id=r.json()["data"][0]["id"]
        r=self.obj.get_v(14,id,self.f1,self.f2)
        self.write2excel(r,14,self.f2)
        # 维度值上移
        r = self.obj.get_v(15, id, self.f1, self.f2)
        self.write2excel(r, 15, self.f2)
    def test_003(self):
        #查询收入中心维度列表
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)

    def test_004(self):
        #新增物业维度
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        tagType=r.json()["data"]["demensionType"]
        #编辑维度
        typeName=r.json()["data"]["typeName"]
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("typeName")
        li.append(typeName)
        l.append("id")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #维度排序上移
        l=[]
        li=[]
        l.append("dimensionTypeId")
        li.append(id)
        l.append("tagType")
        li.append(tagType)
        r=self.obj.post_c(8,self.f1,self.f2,l,li)
        self.write2excel(r,8,self.f2)
        #维度下移
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #新增维度值
        l = []
        li = []
        l.append("dimensionTypeId")
        li.append(id)
        r = self.obj.post_c(11, self.f1, self.f2, l, li)
        self.write2excel(r, 11, self.f2)
        # 编辑维度值
        id1=r.json()["data"]["id"]
        labelDefault=r.json()["data"]["labelDefault"]
        dimensionValue=r.json()["data"]["dimensionTypeId"]
        remark=r.json()["data"]["remark"]
        l=[]
        li=[]
        l.append("id")
        li.append(id1)
        l.append("labelDefault")
        li.append(labelDefault)
        l.append("dimensionValue")
        li.append(dimensionValue)
        l.append("remark")
        li.append(remark)
        r = self.obj.post_c(12,self.f1,self.f2,l,li)
        self.write2excel(r, 12, self.f2)
        #删除维度值
        r=self.obj.post_v(13,id1,self.f1,self.f2)
        self.write2excel(r,13,self.f2)
        #删除维度
        r=self.obj.post_v(6,id,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
    def test_007(self):
        #新增收入中心维度
        r=self.obj.post_t(7,self.f1,self.f2)
        self.write2excel(r,7,self.f2)
        id = r.json()["data"]["id"]
        self.obj.post_v(6, id, self.f1, self.f2)

if __name__ == '__main__':
    unittest.main()