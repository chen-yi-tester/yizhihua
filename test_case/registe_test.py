from page.app import App


class Test_registe:
	result = None
	def setup(self):
		self.result = App.start().getin_my().go_regite().user_registe()
	def test_todo(self):
		assert self.result =='注册成功'
	def teardown(self):
		App.driver.quit()