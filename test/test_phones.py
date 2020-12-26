import re
import pytest
import allure

def test_phones_on_home_page(app):
    with allure.step('Given a user from home and edit page'):
        user_from_home_page = app.user.get_user_list()[0]
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the user from home page is equal to the user from edit page '):
        assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)

def test_phones_on_view_page(app):
    with allure.step('Given a user from home and edit page'):
        user_from_view_page = app.user.get_user_from_view_page(0)
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the user from home page is equal to the user from edit page '):
        assert user_from_view_page.phone_home == user_from_edit_page.phone_home
        assert user_from_view_page.phone_mobile == user_from_edit_page.phone_mobile
        assert user_from_view_page.phone_work == user_from_edit_page.phone_work
        assert user_from_view_page.phone2 == user_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [user.phone_home, user.phone_mobile, user.phone_work, user.phone2]))))