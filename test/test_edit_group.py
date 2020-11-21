# -*- coding: utf-8 -*-

from model.configurations_group import Configurations_group

def test_case(app):
    if app.group.count() == 0:
        app.group.create(Configurations_group(name="New group", header="Add group"))
    app.group.edit_first_group(Configurations_group(name="new", header="new Test", footer="new Test"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Configurations_group(name="New group", header="Add group"))
    app.group.modify_first_group(Configurations_group(name="new_name"))
