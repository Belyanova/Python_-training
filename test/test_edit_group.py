# -*- coding: utf-8 -*-
from random import randrange
from model.configurations_group import Configurations_group

def test_case(app):
    group = Configurations_group(name="new", header="new Test", footer="new Test")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index,group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Configurations_group.id_or_max) == sorted(new_groups,key=Configurations_group.id_or_max)


"""def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Configurations_group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""