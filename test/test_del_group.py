# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group
import random
import pytest
import allure

def test_delete_some_group(app, db, check_ui,json_groups):
    group = json_groups
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list())  == 0:
            app.group.create(group)
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        assert len(old_groups) - 1 == app.group.count()
        new_groups = db.get_group_list()
        old_groups.remove(group)
        #assert old_groups == new_groups
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(old_groups, key=Configurations_group.id_or_max)
