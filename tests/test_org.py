from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_org(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_org.json"
        self.f2="data_org.xls"
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
        #获取组织机构层级树
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #新增组织机构层级
        parentId=r.json()["data"]["listTree"][0]["id"]
        l=[]
        li=[]
        l.append("parentId")
        li.append(parentId)
        r=self.obj.post_c(3,self.f1,self.f2,l,li)
        self.write2excel(r,3,self.f2)
        # 编辑组织机构层级
        r1=self.obj.get_v(8,parentId,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
        total=len(r1.json()["data"]["listTree"])-1
        id=r1.json()["data"]["listTree"][total]["id"]
        nodeName1=r.json()["data"]["nodeName1"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("nodeName1")
        li.append(nodeName1)
        r=self.obj.post_c(4,self.f1,self.f2,l,li)
        self.write2excel(r,4,self.f2)
        #已绑定物业列表
        l=[]
        li=[]
        l.append("deptId")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        # 未绑定物业列表
        l = []
        li = []
        l.append("deptId")
        li.append(id)
        r = self.obj.post_c(6, self.f1, self.f2, l, li)
        self.write2excel(r, 6, self.f2)
        #删除组织机构层级
        r=self.obj.get_v(7,id,self.f1,self.f2)
        self.write2excel(r,7,self.f2)
    def test_009(self):
        #物业绑定 / 解绑
        r = self.obj.post_t(9,self.f1, self.f2)
        self.write2excel(r, 9, self.f2)
        # 组织机构上、下移动

if __name__ == '__main__':
    unittest.main()
