from page.app import App
from page.main_page import MainPage


class Test_login:
	result = None
	def setup(self):
		driver1 = App.start().getin_my().user_login()
		self.result = MainPage(driver1).get_sellerStore().getin_store().buy_now().payOrder_withNecture()

	def test_todo(self):
		assert self.result =='1'
	def teardown(self):
		App.driver.quit()