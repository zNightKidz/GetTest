import requests
import unittest
import json

class myTestCase(unittest.TestCase):

    def setUp(self):
        print("start test")
        pass
    def tearDown(self):
        print("end test")
        pass

class test_case_Device(myTestCase):

    #获取交换机设备信息
    def test_device_get(self):
        self.url = "http://192.168.8.2:8888/system/device"
        self.req = requests.get(url=self.url)
        print("状态吗:",self.req.status_code)
        print("返回值:",self.req.text)
        self.assertEqual(201,self.req.status_code)
        self.assertEqual(0,self.req.text.status)

