# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from configurations_login import Configurations_login
from configurations_group import Configurations_group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/index.php")

    def login(self, wd, configurations_login):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(configurations_login.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(configurations_login.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, configurations_group):
        # Создаем новую группу
        wd.find_element_by_xpath("(//input[@name='new'])[2]").click()
        # Заполняем форму группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(configurations_group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(configurations_group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(configurations_group.footer)
        # Нажимаем на кнопку
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Configurations_login(username="admin", password="secret"))
        self.open_groups_page(wd)
        self.create_group(wd, Configurations_group(name="Test", header="Test", footer="Test"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Configurations_login(username="admin", password="secret"))
        self.open_groups_page(wd)
        self.create_group(wd, Configurations_group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
