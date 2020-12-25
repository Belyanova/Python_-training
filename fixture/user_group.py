from selenium.webdriver.support.ui import Select
from model.configurations_user import Configurations_user
from model.configurations_group import Configurations_group

class UserGroupHelper:
    def __init__(self, app):
        self.app = app

    def group_selection(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group)

    def open_users_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and (wd.find_elements_by_xpath("//form[2]/div[1]/input"))):
            wd.find_element_by_link_text("home").click()

    user_cache = None

    def get_user_in_group_list(self):
        wd = self.app.wd
        if self.user_cache is None:
            wd = self.app.wd
            self.user_cache = []
            for elements in wd.find_elements_by_name("entry"):
                text = elements.find_elements_by_xpath(".//td")
                firstname = text[2].text
                last_name = text[1].text
                user_name = (text[1].text + text[2].text)
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                all_phones = text[5].text
                address = text[3].text
                all_mail = text[4].text
                self.user_cache.append(Configurations_user(user_name=user_name, id=id,address=address,last_name=last_name,
                                        firstname=firstname, all_mail=all_mail, all_phones_from_home_page=all_phones))
        return list(self.user_cache)

    def del_user_in_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.user_cache = None

    def user_add_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group)
        wd.find_element_by_name("add").click()

    def select_user_by_id(self, id):
        wd = self.app.wd
        self.open_users_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_user_in_group(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()