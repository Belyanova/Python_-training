# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login

def test_delete_first_group(app):
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.group.delete_first_group()
    app.session.logout()