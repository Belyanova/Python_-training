# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from Configurations import *


class User(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_start_page(self, wd):
        wd.get("http://localhost/index.php")

    def login(self, wd, Configurations):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(Configurations.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(Configurations.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def add_new_user(self, wd, Configurations):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Configurations.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Configurations.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Configurations.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Configurations.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Configurations.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Configurations.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Configurations.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Configurations.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Configurations.phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Configurations.phone_work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Configurations.mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Configurations.mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Configurations.mail3)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Configurations.bd_day)
        wd.find_element_by_xpath("//option[@value='1']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Configurations.bd_month)
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Configurations.bd_year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Configurations.aday)
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Configurations.amonth)
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Configurations.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Configurations.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Configurations.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Configurations.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_start_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_user(self):
        wd = self.wd
        self.open_start_page(wd)
        self.login(wd, Configurations_login(username="admin", password="secret"))
        self.add_new_user(wd,Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "Address", "Home", "Notes"))
        self.return_start_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
