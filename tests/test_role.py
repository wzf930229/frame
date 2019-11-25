from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_role(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_role.json"
        self.f2="data_role.xls"
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
        #查询角色列表
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #添加角色
        r=self.obj.post_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        #编辑角色
        level=r.json()["data"]["level"]
        name=r.json()["data"]["name"]
        tenantId=r.json()["data"]["tenantId"]
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("level")
        li.append(level)
        l.append("name")
        li.append(name)
        l.append("tenantId")
        li.append(tenantId)
        l.append("id")
        li.append(id)
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #角色授权加载自定义菜单树
        r=self.obj.get_v(4,id,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #角色授权菜单保存
        l=[]
        li=[]
        l.append("roleId")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #通过角色id查询数据看板范围树
        r=self.obj.get_v(6,id,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #角色授权数据看板保存
        l=[]
        li=[]
        l.append("roleId")
        li.append(id)
        r=self.obj.post_c(7,self.f1,self.f2,l,li)
        self.write2excel(r,7,self.f2)
        #删除角色
        r=self.obj.get_v(8,id,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
if __name__ == '__main__':
    unittest.main()