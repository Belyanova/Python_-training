# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
from random import randrange

def test_case(app,json_users):
    user = json_users
    if app.user.count() == 0:
        app.user.add_new_user(user)
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user.id = old_users[index].id
    app.user.edit_user_by_index(index,user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_user_list()
    old_users[index] = user
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)
