
from page.base_page import Basepage
from page.login_page import Login
from page.seller_store import SellerStore


class MainPage(Basepage):
	__my_button_locator = '941,2200'
	__sellerStore_loacator = '403,2187'
	def getin_my(self):
		self.touch_button(self.__my_button_locator)
		return Login(self.driver)
	def get_sellerStore(self):
		self.touch_button(self.__sellerStore_loacator)
		return SellerStore(self.driver)