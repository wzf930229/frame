from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
import datetime
class test_plan(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_plan.json"
        self.f2="data_plan.xls"
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
        #获取计划任务列表
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        if r.json()["data"]["total"]>0:
            for i in range(0,r.json()["data"]["total"]):
                if r.json()["data"]["rows"][i]["statusName"]=="Enabled":
                    id=r.json()["data"]["rows"][i]["id"]
                    #看板加入定时任务
                    l = []
                    li = []
                    lr = []
                    lr.append("id")
                    l.append("ids")
                    li.append(id)
                    ll = [li]
                    r = self.obj.post_c(9, self.f1, self.f2, l, ll)
                    self.write2excel(r, 9, self.f2)
                    # 计划任务已加入的看板列表
                    r = self.obj.post_c(10, self.f1, self.f2, lr, li)
                    self.write2excel(r, 10, self.f2)
                    # 看板移出计划任务
                    id = r.json()["data"][0]["id"]
                    r = self.obj.get_v(11, id, self.f1, self.f2)
                    self.write2excel(r, 11, self.f2)
                    break


    def test_003(self):
        r=self.obj.post_t(2,self.f1,self.f2)
        print(r.text)
        if r.json()["data"]["total"]>0:
            li = []
            l = []
            id = r.json()["data"]["rows"][0]["id"]
            li.append("id")
            l.append(id)
            condense = r.json()["data"]["rows"][0]["condense"]
            li.append("condense")
            l.append(condense)
            jobStatus = r.json()["data"]["rows"][0]["jobStatus"]
            li.append("jobStatus")
            l.append(jobStatus)
            userEmail = r.json()["data"]["rows"][0]["userEmail"]
            li.append("userEmail")
            l.append(userEmail)
            emailTitle = r.json()["data"]["rows"][0]["emailTitle"]
            li.append("emailTitle")
            l.append(emailTitle)
            jobDesc = r.json()["data"]["rows"][0]["jobDesc"]
            li.append("jobDesc")
            l.append(jobDesc)
            jobName = r.json()["data"]["rows"][0]["jobName"]
            li.append("jobName")
            l.append(jobName)
            cycleType = r.json()["data"]["rows"][0]["cycleType"]
            li.append("cycleType")
            l.append(cycleType)
            #startDate = r.json()["data"]["rows"][0]["startDate"]
            now=datetime.datetime.now()+datetime.timedelta(hours=1)
            startDate=now.strftime("%Y-%m-%d %H:%M:%S")
            print(startDate)
            li.append("startDate")
            l.append(startDate)
            #endDate = r.json()["data"]["rows"][0]["endDate"]
            end=now+datetime.timedelta(hours=6)
            endDate=end.strftime("%Y-%m-%d %H:%M:%S")
            li.append("endDate")
            l.append(endDate)
            # 编辑计划任务
            r = self.obj.post_c(4, self.f1, self.f2, li, l)
            print(r.text)
            self.write2excel(r, 4, self.f2)

    def test_004(self):
        # 新增计划任务
        r = self.obj.post_t(3,self.f1,self.f2)
        self.write2excel(r, 3,self.f2)
        id = r.json()["data"]["id"]
        # 计划任务停用
        r = self.obj.get_v(5, id,self.f1,self.f2)
        self.write2excel(r, 5,self.f2)
        # 计划任务激活
        r = self.obj.get_v(6, id,self.f1,self.f2)
        self.write2excel(r, 6,self.f2)
        # 计划任务详情
        r = self.obj.get_v(7, id,self.f1,self.f2)
        self.write2excel(r, 7,self.f2)
        # 计划任务停用
        r = self.obj.get_v(5, id,self.f1,self.f2)
        # 计划任务删除
        r = self.obj.get_v(8, id,self.f1,self.f2)
        self.write2excel(r, 8,self.f2)
if __name__ == '__main__':
    unittest.main()
