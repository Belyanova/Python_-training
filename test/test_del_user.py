# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
def test_delete_first_group(app):
    user = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                               "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                               "April", "2000", "Address", "Home", "Notes")
    if app.group.count() == 0:
        app.group.create(Configurations_user(user))
    app.user.delete_first_user()