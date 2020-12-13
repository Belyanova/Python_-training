# -*- coding: utf-8 -*-
from random import randrange
from model.configurations_group import Configurations_group
import random

def test_case(app,db,check_ui,json_groups):
    group = json_groups
    if len(db.get_group_list())  == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id,group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(app.group.get_group_list(),key=Configurations_group.id_or_max)


"""def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Configurations_group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""