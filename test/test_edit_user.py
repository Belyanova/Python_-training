# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login
from model.configurations_user import Configurations_user

def test_case(app):
    user = Configurations_user("new User_name", "new name", "Last_name", "Nickname", "Title", "Company", "new Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "new e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "new Address", "new Home", "Notes")
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.user.edit_first_user(user)
    app.session.logout()