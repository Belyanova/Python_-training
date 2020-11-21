from selenium.webdriver.support.ui import Select

class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_add_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        return wd

    def save_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
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

    def save_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_new_user(self, configurations_user):
        wd = self.open_add_user_page()
        self.fill_in_user(configurations_user)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_start_page()

    def delete_first_user(self):
        wd = self.app.wd
        # выбрать первый контакт
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # удалить первый контакт
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        #wd.switch_to_alert().accept()


    def edit_first_user(self, configurations_user):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # Изменить первый контакт
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_in_user(configurations_user)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def return_start_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout")

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))