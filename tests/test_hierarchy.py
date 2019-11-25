from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_hierarchy(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_hierarchy.json"
        self.f2="data_hierarchy.xls"
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
        #获取报表数据层级树
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r, 2, self.f2)
        #加载层级树子节点
        id=r.json()["data"][0]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r = self.obj.get_c(3,self.f1,self.f2,l,li)
        self.write2excel(r, 3, self.f2)
    def test_004(self):
        #新增类型
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #编辑类型
        dimensionTypeId=r.json()["data"]["id"]
        typeName=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(dimensionTypeId)
        l.append("typeName")
        li.append(typeName)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #新增报表数据层级
        l=[]
        li=[]
        l.append("dimensionTypeId")
        li.append(dimensionTypeId)
        r=self.obj.post_c(6,self.f1,self.f2,l,li)
        self.write2excel(r,6,self.f2)
        #编辑报表数据层级
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("dimensionTypeId")
        li.append(dimensionTypeId)
        r=self.obj.post_c(7,self.f1,self.f2,l,li)
        self.write2excel(r,7,self.f2)
        #已绑定物业列表
        l=[]
        li=[]
        l.append("hierarchyId")
        li.append(dimensionTypeId)
        r=self.obj.post_t(8,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
        #未绑定物业列表
        l = []
        li = []
        l.append("hierarchyId")
        li.append(dimensionTypeId)
        r = self.obj.post_t(9, self.f1, self.f2)
        self.write2excel(r, 9, self.f2)
        # 物业绑定
        shopIds=r.json()["data"]["rows"][0]["id"]
        l=[]
        li=[]
        l.append("shopIds")
        li.append(shopIds)
        l.append("hierarchyId")
        li.append(dimensionTypeId)
        r=self.obj.post_c(10,self.f1,self.f2,l,li)
        self.write2excel(r,10,self.f2)
        #物业解绑
        l=[]
        li=[]
        l.append("ids")
        li.append(dimensionTypeId)
        r=self.obj.post_c(11,self.f1,self.f2,l,li)
        self.write2excel(r,11,self.f2)
        #删除报表数据层级
        r=self.obj.post_v(12,id,self.f1,self.f2)
        self.write2excel(r,12,self.f2)
        #删除类型
        r=self.obj.post_v(13,dimensionTypeId,self.f1,self.f2)
        self.write2excel(r,13,self.f2)
if __name__ == '__main__':
    unittest.main()



