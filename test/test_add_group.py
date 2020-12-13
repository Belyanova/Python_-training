# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group

def test_case(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups[0:2], key=Configurations_group.id_or_max) == sorted(new_groups[0:2], key=Configurations_group.id_or_max)
