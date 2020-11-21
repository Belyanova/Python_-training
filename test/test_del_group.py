# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Configurations_group(name="New group", header="Add group"))
    app.group.delete_first_group()