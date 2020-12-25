from pytest_bdd import given, when, then
from model.configurations_group import Configurations_group
import pytest

@pytest.fixture
@given('a group list')
def group_list(db):
    return db.get_group_list()

@pytest.fixture
@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Configurations_group(name=name, header=header, footer=footer)

@when('I add the group the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    #old_groups = old_groups.append(new_group)
    assert new_groups == old_groups
    assert sorted(new_groups, key=Configurations_group.id_or_max) == sorted(old_groups, key=Configurations_group.id_or_max)