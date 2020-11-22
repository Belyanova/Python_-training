# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user

def test_case(app):
    old_users = app.user.get_user_list()
    user = Configurations_user("new User_name", "new name", "Last_name", "Nickname", "Title", "Company", "new Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "new e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "new Address", "new Home", "Notes")
    if app.group.count() == 0:
        app.group.create(Configurations_user(user))
    user.id = old_users[0].id
    app.user.edit_first_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[0] = user
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

