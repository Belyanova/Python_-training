import pymysql
from fixture.orm import ORM_fixture
from model.configurations_group import  Configurations_group

db = ORM_fixture (host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_users_not_in_group(Configurations_group(id="60"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()