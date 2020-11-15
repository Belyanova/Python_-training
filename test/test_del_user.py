# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login

def test_delete_first_group(app):
    app.user.delete_first_user()