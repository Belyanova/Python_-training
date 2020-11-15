import pytest
from fixture.application import Application
from model.configurations_login import Configurations_login

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login(Configurations_login(username="admin", password="secret"))
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture