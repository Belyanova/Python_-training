# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import random
import pytest
import allure

def test_delete_first_group(app, db, check_ui, json_users):
    user = json_users
    with allure.step('Given a non-empty user list'):
        if len(db.get_user_list()) == 0:
            app.user.add_new_user(user)
        old_users = db.get_user_list()
    with allure.step('Given a random user from the list'):
        user = random.choice(old_users)
    with allure.step('When I delete the user from the list'):
        app.user.delete_user_by_id(user.id)
    with allure.step('Then the new user list is equal to the old list without the deleted user'):
        assert len(old_users) - 1 == app.user.count()
        new_users = db.get_user_list()
        old_users .remove(user)
        assert sorted(new_users , key=Configurations_user.id_or_max) == sorted(old_users, key=Configurations_user.id_or_max)
