from random import randrange
import re

def test_user_on_home_page(app, json_users):
    user = json_users
    if app.user.count() == 0:
        app.user.add_new_user(user)
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user_from_home_page = app.user.get_user_list()[index]
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.user_name == merge_user_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.address == user_from_edit_page.address
    assert user_from_home_page.all_mail == merge_mail_like_on_home_page(user_from_edit_page)


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