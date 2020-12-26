# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import pytest
import allure

def test_user(app, db, check_ui, json_users):
    user = json_users
    with allure.step('Given a user list'):
        old_users = db.get_user_list()
    with allure.step('When I add a user %s the list' % user):
        app.user.add_new_user(user)
    with allure.step('Then the new user list is equal to the old list with the added user'):
        new_users = db.get_user_list()
        old_users.append(user)
        assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

