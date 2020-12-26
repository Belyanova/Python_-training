from pytest_bdd import given, when, then
from model.configurations_user import Configurations_user
import random

@given('a user list', target_fixture="user_list")
def user_list(db):
    return db.get_user_list()

@given('a user', target_fixture="new_user")
def new_user():
    return(Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                               "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                               "April", "2000", "Address", "Home", "Notes"))

@when('I add the user the list')
def add_new_user(app, new_user):
    app.user.add_new_user(new_user)

@then('the new user list is equal to the old list with the added user')
def verify_user_added(db, user_list, new_user):
    old_users = user_list
    new_users = db.get_user_list()
    assert len(new_users) == len(old_users)+1
    old_users.append(new_user)
    assert sorted(new_users, key=Configurations_user.id_or_max) == sorted(old_users, key=Configurations_user.id_or_max)

@given('a non-empty user list', target_fixture="non_empty_user_list")
def non_empty_user_list(app, db):
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                               "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                               "April", "2000", "Address", "Home", "Notes"))
    return db.get_user_list()

@given('a random user from the list', target_fixture="random_user")
def random_user(non_empty_user_list):
    return random.choice(non_empty_user_list)

@when('I delete the user from the list')
def delete_user(app, random_user):
    app.user.delete_user_by_id(random_user.id)

@then('the new user list is equal to the old list without the deleted user')
def verify_user_dell(db, non_empty_user_list, random_user, app, check_ui):
    old_users = non_empty_user_list
    new_users = db.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(random_user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=Configurations_user.id_or_max) == sorted(app.user.get_user_list(),
                                                                                key=Configurations_user.id_or_max)

@when('I edit the user from the list')
def edit_user(app, random_user):
    app.user.edit_user_by_id(random_user.id, random_user)

@then('the new user list is equal to the old list without the edit user')
def verify_user_dell(db, non_empty_user_list, app, check_ui):
    old_users = non_empty_user_list
    assert len(old_users) == app.user.count()
    new_users = db.get_user_list()
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=Configurations_user.id_or_max) == sorted(app.user.get_user_list(),
                                                                                key=Configurations_user.id_or_max)


