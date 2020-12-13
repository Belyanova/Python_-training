# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import random

def test_case(app, db, check_ui,json_users):
    user = json_users
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user)
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.edit_user_by_id(user.id,user)
    assert len(old_users) == app.user.count()
    new_users = db.get_user_list()
    assert old_users == new_users
    if check_ui:
        assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)
