from time import sleep

from page.base_page import Basepage


class Registe(Basepage):
	__phone_insert = "300,908"
	__phone_insert_id = "com.lxlg.spend.yw.user:id/et_register_phone"
	__smcode_insert = "280,1097"
	__smcode_insert_id = "com.lxlg.spend.yw.user:id/et_register_code"
	__super_input = "991,1382"
	__super_input_id = "com.lxlg.spend.yw.user:id/et_register_referrer"
	__password_insert = "280,1276"
	__password_insert_id = "com.lxlg.spend.yw.user:id/et_register_new_passwd"
	__password_insure = "280,1460"
	__password_insure_id = "com.lxlg.spend.yw.user:id/et_register_sure_passwd"
	__complete_button = "532,1868"
	__close_input = "991,1382"
	__smcode = "1234"
	__password = "123456"
	def user_registe(self):
		phone = Basepage.create_phone(self)
		self.touch_button(self.__phone_insert)
		self.find_by_id(self.__phone_insert_id).send_keys(phone)
		self.touch_button(self.__smcode_insert)
		self.find_by_id(self.__smcode_insert_id).send_keys(self.__smcode)
		self.touch_button(self.__password_insert)
		self.find_by_id(self.__password_insert_id).send_keys(self.__password)
		self.touch_button(self.__close_input)
		self.find_by_id(self.__password_insure_id).send_keys(self.__password)
		self.touch_button(self.__close_input)
		self.touch_button(self.__complete_button)
		sleep(1)
		result=self.get_toast()
		return result