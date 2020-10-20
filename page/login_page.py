from page.base_page import Basepage
from page.registe_page import Registe


class Login(Basepage):
	__go_login_button="510,2008"
	__phone_insert = "126,742"
	__phone_insert_id = "com.lxlg.spend.yw.user:id/et_login_phone"
	__close_input = "991,1382"
	__password_insert = "130,1005"
	__password_insert_id = "com.lxlg.spend.yw.user:id/et_login_passwd"
	__login_button = "541,1464"
	__go_registe_button = "979,150"
	__user_Phone = "18502338733"
	__user_Password = "123456"
	result =""
	def get_login_result(self):
		self.touch_button(self.__go_login_button)
		self.touch_button(self.__phone_insert)
		self.find_by_id(self.__phone_insert_id).send_keys(self.__user_Phone)
		self.touch_button(self.__password_insert)
		self.find_by_id(self.__password_insert_id).send_keys(self.__user_Password)
		#关闭输入法窗口
		self.touch_button(self.__close_input)
		self.touch_button(self.__login_button)
		self.result=self.get_toast()
		return self.result
	def user_login(self):
		self.touch_button(self.__go_login_button)
		self.touch_button(self.__phone_insert)
		self.find_by_id(self.__phone_insert_id).send_keys(self.__user_Phone)
		self.touch_button(self.__password_insert)
		self.find_by_id(self.__password_insert_id).send_keys(self.__user_Password)
		# 关闭输入法窗口
		self.touch_button(self.__close_input)
		self.touch_button(self.__login_button)
		return self.driver
	def go_regite(self):
		self.touch_button(self.__go_login_button)
		self.touch_button(self.__go_registe_button)
		return Registe(self.driver)