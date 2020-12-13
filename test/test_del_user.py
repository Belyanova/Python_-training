# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import random

def test_delete_first_group(app, db, check_ui, json_users):
    user = json_users
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user)
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    assert len(old_users) - 1 == app.user.count()
    new_users = db.get_user_list()
    old_users .remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users , key=Configurations_user.id_or_max) == sorted(app.user.get_group_list(), key=Configurations_user.id_or_max)
