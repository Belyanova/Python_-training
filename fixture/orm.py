from datetime import datetime
from pony.orm import *
from model.configurations_group import Configurations_group
from model.configurations_user import Configurations_user
from pymysql.converters import decoders

class ORM_fixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        users = Set(lambda: ORM_fixture.ORMuser, table="address_in_groups",column="id", reverse="groups")#, lasy=True)

    class ORMuser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional (str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORM_fixture.ORMGroup, table="address_in_groups", column="group_id", reverse="users")#, lasy=True)

    def __init__(self,host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password) #, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self,groups):
        def convert(group):
            return Configurations_group (id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_users_to_model(self,users):
        def convert(user):
            return Configurations_user(id=str(user.id), last_name=user.lastname, firstname=user.firstname)
        return list(map(convert, users))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORM_fixture.ORMGroup))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(c for c in ORM_fixture.ORMuser if c.deprecated is None))

    @db_session
    def get_users_in_group(self, group):
        orm_group = list(select(g for g in ORM_fixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(orm_group.users)

    @db_session
    def get_users_not_in_group(self, group):
        orm_group = list(select(g for g in ORM_fixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(c for c in ORM_fixture.ORMuser if c.deprecated is None and orm_group not in c.groups))