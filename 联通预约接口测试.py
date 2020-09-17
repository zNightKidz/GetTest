import requests


#获取所有城市站点的信息
# url="http://140.143.191.187:38097/multimedia/platform/api/v1/facility/all"
# response = requests.get(url)
# strAllFacility ='''[{"facilityId":2,"name":"Beijing-AG1","building":""},{"facilityId":3,"name":"Beijing-AG2","building":""},{"facilityId":4,"name":"Beijing-BB1","building":""},{"facilityId":5,"name":"Beijing-BB2","building":""},{"facilityId":30,"name":"CCTV","building":null},{"facilityId":23,"name":"ChangSha-BB","building":null},{"facilityId":24,"name":"ChangSha-User","building":null},{"facilityId":6,"name":"ChengDu-BB","building":""},{"facilityId":7,"name":"FuZhou-BB","building":""},{"facilityId":8,"name":"GuangZhou-BB","building":""},{"facilityId":26,"name":"HangZhou-BB","building":null},{"facilityId":25,"name":"HangZhou-User","building":null},{"facilityId":15,"name":"HongKong-BB","building":""},{"facilityId":16,"name":"London-BB","building":""},{"facilityId":17,"name":"LosAngeles-BB","building":""},{"facilityId":27,"name":"Mobile-1","building":null},{"facilityId":28,"name":"Mobile-2","building":null},{"facilityId":21,"name":"NewYork-BB","building":null},{"facilityId":29,"name":"Satellite","building":null},{"facilityId":9,"name":"ShangHai-BB","building":""},{"facilityId":10,"name":"ShenYang-BB","building":""},{"facilityId":22,"name":"Sydney-BB","building":null},{"facilityId":11,"name":"TianJin-BB","building":""},{"facilityId":12,"name":"TianJin-User","building":""},{"facilityId":18,"name":"Tokyo-BB","building":""},{"facilityId":19,"name":"Urumchi-BB","building":null},{"facilityId":20,"name":"Urumchi-User","building":null},{"facilityId":13,"name":"WuHan-BB","building":""},{"facilityId":14,"name":"XiAn-BB","building":""}]'''
#
# print("response的text内容：",response.text)
# print("response.text的类型是：",type(response.text))
# print("response.status_code值：",response.status_code)
# print("response.headers返回值",response.headers)
# print("response.request返回值",response.request)
# print(response.text.find(strAllFacility))
# print(response.text.index(strAllFacility))

#获取所有城市站点的信息
def GetAllFacility():
    url = 'http://140.143.191.187:38097/multimedia/platform/api/v1/facility/all'
    response = requests.get(url)
    strAllFacility = '''[{"facilityId":2,"name":"Beijing-AG1","building":""},{"facilityId":3,"name":"Beijing-AG2","building":""},{"facilityId":4,"name":"Beijing-BB1","building":""},{"facilityId":5,"name":"Beijing-BB2","building":""},{"facilityId":30,"name":"CCTV","building":null},{"facilityId":23,"name":"ChangSha-BB","building":null},{"facilityId":24,"name":"ChangSha-User","building":null},{"facilityId":6,"name":"ChengDu-BB","building":""},{"facilityId":7,"name":"FuZhou-BB","building":""},{"facilityId":8,"name":"GuangZhou-BB","building":""},{"facilityId":26,"name":"HangZhou-BB","building":null},{"facilityId":25,"name":"HangZhou-User","building":null},{"facilityId":15,"name":"HongKong-BB","building":""},{"facilityId":16,"name":"London-BB","building":""},{"facilityId":17,"name":"LosAngeles-BB","building":""},{"facilityId":27,"name":"Mobile-1","building":null},{"facilityId":28,"name":"Mobile-2","building":null},{"facilityId":21,"name":"NewYork-BB","building":null},{"facilityId":29,"name":"Satellite","building":null},{"facilityId":9,"name":"ShangHai-BB","building":""},{"facilityId":10,"name":"ShenYang-BB","building":""},{"facilityId":22,"name":"Sydney-BB","building":null},{"facilityId":11,"name":"TianJin-BB","building":""},{"facilityId":12,"name":"TianJin-User","building":""},{"facilityId":18,"name":"Tokyo-BB","building":""},{"facilityId":19,"name":"Urumchi-BB","building":null},{"facilityId":20,"name":"Urumchi-User","building":null},{"facilityId":13,"name":"WuHan-BB","building":""},{"facilityId":14,"name":"XiAn-BB","building":""}]'''
    print("response.status_code值：",response.status_code)
    foo = response.text.find(strAllFacility)
    print("foo的类型为：",type(foo))
    print("起始位置为：",foo)
    assert foo != -1,"接口异常！"



if __name__=="__main__":
    GetAllFacility()



