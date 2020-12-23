from model.configurations_user import Configurations_user
import random

def test_user_del_group(app, db):
    groups = db.get_group_list()
    group = random.choice(groups)
    group = group.name
    app.user.group_selection(group)
    users_from_page = app.user.get_user_in_group_list(group)
    if len(users_from_page) == 0:
        user_new = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address",
                                   "999888777",
                                   "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998",
                                   "1",
                                   "April", "2000", group, "Address", "Home", "Notes")
        app.user.add_new_user(user_new)
        app.user.open_users_page()
    app.user.group_selection(group)
    user = random.choice(users_from_page)
    app.user.select_user_by_id(user.id)
    app.user.del_user_in_group()
    users_new = app.user.get_user_in_group_list(group)
    assert len(users_from_page) - 1 == len(users_new)