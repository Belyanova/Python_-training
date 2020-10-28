# -*- coding: utf-8 -*-
from new_user import User_info
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class User(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/index.php")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def add_new_user(self, wd, new_user):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(User_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(phone_work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(mail3)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bd_day)
        wd.find_element_by_xpath("//option[@value='1']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bd_month)
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(bd_year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.add_new_user(wd, User_info(User_name="User_name", middlename="name", last_name="Last_name", nickname="Nickname",title="Title", company="Company", address="Address", phone_home="999888777", phone_mobile="12345678",
                 phone_work="87654321", mail1="e-mail_1", mail2="e-mail_2", mail3="e-mail_3", bd_day="1", bd_month="April",
                 bd_year="1998", aday="1", amonth="April", ayear="2000", address2="Address", phone2="Home",
                 notes="Notes"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
