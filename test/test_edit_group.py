# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login
from model.configurations_group import Configurations_group

def test_case(app):
    app.group.edit_first_group(Configurations_group(name="new", header="new Test", footer="new Test"))

def test_modify_group_name(app):
    app.group.modify_first_group(Configurations_group(name="new_name"))
