# -*- coding: utf-8 -*-
from model.configurations_group import Configurations_group


def test_case(app):
    app.group.create(Configurations_group(name="Test", header="Test", footer="Test"))


def test_add_empty_group(app):
    app.group.create(Configurations_group(name="", header="", footer=""))
