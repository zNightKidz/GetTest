import requests

def get_one_page(url):
	try:
		response = requests.get(url,timeout = 30)
		response.raise_for_status()
		response.encoding = response.apparent.encoding
		return response.text()

	except:
		print('产生异常')
		return ''

if __name__ == '__main__':
	main()