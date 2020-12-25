import pymysql
from model.configurations_group import Configurations_group
from model.configurations_user import Configurations_user
from model.user_in_group import UserGroup

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name , user=user , password=password, autocommit=True )

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Configurations_group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, nickname, title, company, address, home,"
                           "mobile, work, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, title, company, address, home, mobile, work,
                 email, email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2,phone2, notes) = row
                list.append(Configurations_user(id=str(id), firstname=firstname, last_name=lastname, middlename=middlename,
                nickname=nickname, title = title, company = company, address = address,phone_home = home, phone_mobile = mobile,
                bd_day = str(bday),bd_month = bmonth,bd_year= byear, aday=str(aday), amonth=amonth, ayear=ayear,
                phone_work = work, mail1 = email, mail2 = email2, mail3 = email3, address2 = address2, phone2 = phone2, notes = notes))
        finally:
            cursor.close()
        return list

    def get_user_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(UserGroup(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()