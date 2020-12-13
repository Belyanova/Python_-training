# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user

def test_user(app, db, check_ui, json_users):
    user = json_users
    old_users = db.get_user_list()
    app.user.add_new_user(user)
    new_users = db.get_user_list()
    old_users.append(user)
    if check_ui:
        assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

