# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group
import pytest
import allure

def test_case(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(old_groups,key=Configurations_group.id_or_max)