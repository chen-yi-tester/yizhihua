from time import sleep

from page.base_page import Basepage
from page.store_detail import StoreDetail


class SellerStore(Basepage):
	__storeName_insert = "490,143"
	__storeName_insert_id = "com.lxlg.spend.yw.user:id/et_search_content"
	__find_button = "991,1718"
	__store_name = "帽子带好"
	__store_locator = "220,565"
	def getin_store(self):
		self.touch_button(self.__storeName_insert)
		self.find_by_id(self.__storeName_insert_id).send_keys(self.__store_name)
		self.touch_button(self.__find_button)
		sleep(3)
		self.touch_button(self.__store_locator)
		return StoreDetail(self.driver)