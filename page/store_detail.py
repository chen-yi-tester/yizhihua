from page.base_page import Basepage
from page.sellerOrder_detail import SellerOrderDetail


class StoreDetail(Basepage):
	__buyNow_locator = '534,2200'
	def buy_now(self):
		self.touch_button(self.__buyNow_locator)
		return SellerOrderDetail(self.driver)