# -*- coding: utf-8 -*-

from model.configurations_group import Configurations_group

def test_case(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Configurations_group(name="New group", header="Add group"))
    group = Configurations_group(name="new", header="new Test", footer="new Test")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0]=group
    assert sorted(old_groups, key=Configurations_group.id_or_max) == sorted(new_groups,key=Configurations_group.id_or_max)


"""def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Configurations_group(name="New group", header="Add group"))
    app.group.modify_first_group(Configurations_group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""