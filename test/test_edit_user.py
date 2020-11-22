# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user

def test_case(app):
    user = Configurations_user("new User_name", "new name", "Last_name", "Nickname", "Title", "Company", "new Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "new e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "new Address", "new Home", "Notes")
    if app.user.count() == 0:
        app.user.add_new_user(user)
    old_users = app.user.get_user_list()
    user.id = old_users[0].id
    app.user.edit_first_user(user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_user_list()
    old_users[0] = user
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)
