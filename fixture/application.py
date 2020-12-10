from selenium import webdriver
from fixture.session import SessionHelper
from fixture.user import UserHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/index.php")

    def destroy(self):
        self.wd.quit()