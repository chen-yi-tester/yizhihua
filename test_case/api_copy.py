from page.req_copy import request_method

req = request_method()

class api_lists:
	test_host = 'lxlgyzh.f3322.net:2222'
	login_url = test_host+'/user/Auth/userLogin'
	user_account = '18502338722'
	password = 'BE56E057F20F883EE10ADC3949BA59AB'
	unionId = ''
	verifyCode = ''
	deviceNumber = req.create_phone()
	@classmethod
	def old_user_login(self):
		r= req.get(url=self.login_url,params={"user_account":self.user_account,"password":self.password,\
		'unionId':self.unionId,'verifyCode':self.verifyCode,'deviceNumber':self.deviceNumber})
		print(r)