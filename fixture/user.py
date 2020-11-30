﻿from selenium.webdriver.support.ui import Select
from model.configurations_user import Configurations_user
import re

class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_users_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and (wd.find_elements_by_xpath("//form[2]/div[1]/input"))):
            wd.find_element_by_link_text("home").click()

    def open_add_user_page(self):
        wd = self.app.wd
        if not wd.find_elements_by_name("photo"):
            wd.find_element_by_link_text("add new").click()
        return wd

    def save_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath('(//input[@name="submit"])[2]').click()

    def fill_in_user(self, configurations_user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(configurations_user.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(configurations_user.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(configurations_user.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(configurations_user.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(configurations_user.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(configurations_user.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(configurations_user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(configurations_user.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(configurations_user.phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(configurations_user.phone_work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(configurations_user.mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(configurations_user.mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(configurations_user.mail3)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(configurations_user.bd_day)
        wd.find_element_by_xpath("//option[@value='1']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(configurations_user.bd_month)
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(configurations_user.bd_year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(configurations_user.aday)
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(configurations_user.amonth)
        wd.find_element_by_xpath("(//option[@value='April'])").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(configurations_user.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(configurations_user.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(configurations_user.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(configurations_user.notes)

    def add_new_user(self, configurations_user):
        wd = self.app.wd
        self.open_add_user_page()
        self.fill_in_user(configurations_user)
        wd.find_element_by_xpath('(//input[@name="submit"])[2]').click()
        self.return_start_page()
        self.user_cache = None

    def select_first_user(self):
        wd = self.app.wd
        self.select_user_by_index(0)

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self,index):
        wd = self.app.wd
        # выбрать первый контакт
        wd.find_element_by_link_text("home").click()
        self.select_user_by_index(index)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.user_cache = None

    def edit_first_user(self):
        self.edit_user_by_index(0)

    def open_edit_user_by_index(self, index):
        wd = self.app.wd
        self.open_users_page()
        self.select_user_by_index(index)
        wd.find_elements_by_xpath('//img[@alt="Edit"]')[index].click()

    def open_view_user_by_index(self, index):
        wd = self.app.wd
        self.open_users_page()
        self.select_user_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def edit_user_by_index(self, index, configurations_user):
        wd = self.app.wd
        self.open_edit_user_by_index(index)
        self.fill_in_user(configurations_user)
        wd.find_element_by_xpath('(//input[@name="update")[2]').click()
        self.user_cache = None

    def return_start_page(self):
        wd = self.app.wd
        if wd.find_element_by_link_text("home page"):
            wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout")

    def count(self):
        wd = self.app.wd
        self.open_users_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_users_page()
            self.user_cache = []
            for elements in wd.find_elements_by_name("entry"):
                text = elements.find_elements_by_xpath(".//td")
                last_name = text[1].text
                firstname = text[2].text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                all_phones = text[5].text.splitlines()
                self.user_cache.append(Configurations_user(last_name=last_name, firstname=firstname, id=id,
                phone2 = all_phones[3],phone_home = all_phones[0], phone_mobile = all_phones[1], phone_work = all_phones[2]))
        return list(self.user_cache)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_user_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Configurations_user(firstname=firstname, last_name=last_name, phone2=phone2,
                                   phone_home=phone_home, phone_mobile=phone_mobile,phone_work=phone_work, id=id)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_user_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Configurations_user(phone2=phone2, phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work)