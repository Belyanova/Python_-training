# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group
import random

def test_delete_some_group(app, db, check_ui,json_groups):
    group = json_groups
    if len(db.get_group_list())  == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(app.group.get_group_list(), key=Configurations_group.id_or_max)
