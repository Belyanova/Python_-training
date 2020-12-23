import re
from model.configurations_user import Configurations_user

def test_user_on_home_page(app, db, json_users):
    user = json_users
    if app.user.count() == 0:
        app.user.add_new_user(user)
    users_from_home_page = app.user.get_user_list()
    users_from_db = db.get_user_list()
    assert len(users_from_home_page) == len(users_from_db)
    #assert sorted(users_from_home_page, key=Configurations_user.id_or_max) == sorted(users_from_db, key=Configurations_user.id_or_max)
    for i in range(len(users_from_home_page)):
        user_from_home_page_by_index = sorted(app.user.get_user_list(), key=Configurations_user.id_or_max)[i]
        user_from_db_by_index = db.get_user_list()[i]
        assert user_from_home_page_by_index.user_name == merge_user_like_on_home_page(user_from_db_by_index)
        assert user_from_home_page_by_index.all_mail == merge_mail_like_on_home_page(user_from_db_by_index)
        assert user_from_home_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_db_by_index)



def clear(s):
    return re.sub("[()-]","",s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [user.phone_home, user.phone_mobile, user.phone_work, user.phone2]))))

def merge_user_like_on_home_page(user):
    return "".join(filter(lambda x: x != "",filter(lambda x: x is not None,
                                [user.last_name, user.firstname])))

def merge_mail_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",filter(lambda x: x is not None,
                                [user.mail1, user.mail2, user.mail3])))