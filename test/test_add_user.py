# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user

def test_user(app,json_users):
    user = json_users
    old_users = app.user.get_user_list()
    app.user.add_new_user(user)
    assert len(old_users)+1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

