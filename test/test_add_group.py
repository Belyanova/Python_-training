# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group


def test_case(app):
    group = Configurations_group(name="Test", header="Test", footer="Test")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Configurations_group.id_or_max) == sorted(new_groups, key=Configurations_group.id_or_max)


def test_add_empty_group(app):
    group = Configurations_group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Configurations_group.id_or_max) == sorted(new_groups,key=Configurations_group.id_or_max)