# -*- coding: utf-8 -*-
from random import randrange
from model.configurations_group import Configurations_group
import random
import pytest
import allure

def test_case(app,db,check_ui,json_groups):
    group = json_groups
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list())  == 0:
            app.group.create(group)
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I edit the group from the list'):
        app.group.edit_group_by_id(group.id,group)
    with allure.step('Then the new group list is equal to the old list without the edit group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(app.group.get_group_list(),key=Configurations_group.id_or_max)


"""def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Configurations_group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""