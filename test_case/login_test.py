from page.app import App

class Test_login:
	result = None
	def setup(self):
		self.result = App.start().getin_my().get_login_result()
	def test_todo(self):
		assert self.result =='登录成功!'
	def teardown(self):
		App.driver.quit()