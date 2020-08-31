import requests,json
import unittest

params = "q=TomCruise" # 汤姆·克鲁斯的电影
url = "https://api.douban.com/v2/movie/search?"

try:
	req = requests.get(url+params)
	req = json.dumps(req.json(),ensure_ascii=False,indent=4)		
except requests.RequestException as e:
	raise
name = "汤姆·克鲁斯"

if name in req:
	print("测试通过")
else:
	print("测试不通过")

# class demo(unittest.TestCase):
# 	"""docstring for demo"""
# 	def setUp(self):
# 		self.url = "https://api.douban.com/v2/movie/search?"
# 		self.actor_name = "q=TomCruise"
# 		self.style_tag = "tag=爱情"
# 		self.name = "TomCruise"
# 		self.action = ""

# 	def test_actor(self):
# 		req = requests.get(self.url+self.actor_name)
# 		req = json.dumps(req.json(),ensure_ascii=False,indent=4)
# 		self.assertIn(self.name,req,msg=None)

# 	def test_style_tag(self):
# 		req = requests.get(self.url+self.actor_name)
# 		req =json.dumps(req.json(),ensure_ascii=False,indent=4)
# 		self.assertIn(self.action,req,msg=None)

# if __name__ == '__main__':
# 	unittest.main()
