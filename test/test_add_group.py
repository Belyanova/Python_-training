# -*- coding: utf-8 -*-
import pytest
from model.configurations_login import Configurations_login
from model.configurations_group import Configurations_group
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_case(app):
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.group.create(Configurations_group(name="Test", header="Test", footer="Test"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.group.create(Configurations_group(name="", header="", footer=""))
    app.session.logout()
