# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Configurations_user(firstname=random_string("firstname", 3), middlename=random_string("middlename", 5),
                        last_name=random_string("last_name", 3), nickname=random_string("nickname", 5),
                        title=random_string("title", 3), company=random_string("company", 5),
                        address=random_string("address", 3), phone_home=random_string("phone_home", 5),
                        phone_mobile=random_string("phone_mobile", 3), phone_work=random_string("phone_work", 5),
                        mail1=random_string("mail1", 3), mail2=random_string("mail2", 5),mail3=random_string("mail3", 3),
                        bd_day="1", bd_month="April",bd_year="1998",aday="1",amonth="April",ayear="2000",
                        address2=random_string("address2", 5),
                        phone2=random_string("phone2", 3),notes = random_string("notes", 5))
]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_user(app,user):
    old_users = app.user.get_user_list()
    app.user.add_new_user(user)
    assert len(old_users)+1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

