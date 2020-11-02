# -*- coding: utf-8 -*-
import pytest
from configurations_login import Configurations_login
from configurations_group import Configurations_group
from application_group import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_case(app):
    app.login(Configurations_login(username="admin", password="secret"))
    app.create_group(Configurations_group(name="Test", header="Test", footer="Test"))
    app.logout()

def test_add_empty_group(app):
    app.login(Configurations_login(username="admin", password="secret"))
    app.create_group(Configurations_group(name="", header="", footer=""))
    app.logout()
