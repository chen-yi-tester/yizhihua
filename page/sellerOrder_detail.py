from page.base_page import Basepage


class SellerOrderDetail(Basepage):
	__price_insert = "500,314"
	__price_insert_id = "com.lxlg.spend.yw.user:id/tv_pay_money"
	__necture_button = "962,855"
	__pay_button = '900,2213'
	__pay_button_id = 'com.lxlg.spend.yw.user:id/tv_commit_order'
	__price = '1'
	__pay_success_id = 'com.lxlg.spend.yw.user:id/tvPrice'
	__close_input = "991,1382"
	def payOrder_withNecture(self):
		self.touch_button(self.__price_insert)
		self.find_by_id(self.__price_insert_id).send_keys(self.__price)
		self.touch_button(self.__close_input)
		self.touch_button(self.__necture_button)
		self.driver.find_element_by_id(self.__pay_button_id).click()
		self.pay_password()
		result = self.get_text_by_id(self.__pay_success_id)
		return result