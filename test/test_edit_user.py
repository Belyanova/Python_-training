# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login

def test_case(app):
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.user.edit_first_user()
    app.session.logout()