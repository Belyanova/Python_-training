from model.configurations_user import Configurations_user
from model.configurations_group import Configurations_group
import random

def test_user_dell_group(app, db):
    #Данные для заполнения
    user_new = Configurations_user("User_name2", "name", "Last_name", "Nickname", "Title", "Company", "Address",
                                   "999888777",
                                   "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998",
                                   "1",
                                   "April", "2000", "Address", "Home", "Notes")
    group_new = Configurations_group("name", "header","footer")
    #Проверки
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user_new)
        app.user.open_users_page()
    all_user = db.get_user_list()
    if len(db.get_group_list()) == 0:
        app.group.create(group_new)
    list_group = db.get_group_list()
    group = random.choice(list_group)
    app.user.open_users_page()
    #Открыть страницу рандомной группы
    app.UserGroup.group_selection(group.name)
    #Список контактов на ней
    list_user_in_group = app.UserGroup.get_user_in_group_list()
    #Проверка списка
    if len(list_user_in_group) == 0:
        #Добавляем случайного пользователя в группу
        user_add_group = random.choice(all_user)
        app.UserGroup.select_user_by_id(user_add_group.id)
        app.UserGroup.user_add_group(group.name)
    app.UserGroup.open_users_page()
    app.UserGroup.group_selection(group.name)
    # Список контактов на ней
    list_user_in_group = db.get_user_in_group_list()
    #Выбираем случайный контакт
    user_dell_group = random.choice(list_user_in_group)
    app.UserGroup.select_user_in_group(user_dell_group.id)
    app.UserGroup.del_user_in_group()
    list_user_in_group_new = db.get_user_in_group_list()
    assert len(list_user_in_group_new) == len(list_user_in_group) - 1


