﻿# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login
from model.configurations_group import Configurations_group

def test_case(app):
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.group.edit_first_group(Configurations_group(name="new", header="new Test", footer="new Test"))
    app.session.logout()