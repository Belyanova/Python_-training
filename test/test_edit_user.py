# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import re
import random
import pytest
import allure

def test_case(app, db, check_ui,json_users):
    user = json_users
    with allure.step('Given a non-empty user list'):
        if len(db.get_user_list()) == 0:
            app.user.add_new_user(user)
        old_users = db.get_user_list()
    with allure.step('Given a random user from the list'):
        user = random.choice(old_users)
    with allure.step('When I edit the user from the list'):
        app.user.edit_user_by_id(user.id,user)
    with allure.step('Then the new user list is equal to the old list without the edit user'):
        assert len(old_users) == app.user.count()
        new_users = db.get_user_list()
        assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

def clear(s):
    return re.sub("[() -]","",s)