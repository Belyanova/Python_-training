from pytest_bdd import scenario
from .user_steps import *

@scenario('users.feature', 'Add new user')
def test_add_new_user():
    pass

@scenario('users.feature', 'Delete a user')
def test_delete_user():
    pass

@scenario('users.feature', 'Edit a user')
def test_edit_user():
    pass