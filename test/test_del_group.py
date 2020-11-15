# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login

def test_delete_first_group(app):
    app.group.delete_first_group()