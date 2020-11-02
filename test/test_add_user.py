# -*- coding: utf-8 -*-
import pytest
from model.configurations_login import Configurations_login
from model.configurations_user import Configurations_user
from fixture.application_user import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_user(app):
    user = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "Address", "Home", "Notes")
    app.session.login(Configurations_login(username="admin", password="secret"))
    app.user.add_new_user(user)
    app.session.logout()
