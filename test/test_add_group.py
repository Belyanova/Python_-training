# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group

def test_case(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(app.group.get_group_list(),key=Configurations_group.id_or_max)