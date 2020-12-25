from model.configurations_group import Configurations_group
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean (group):
        return Configurations_group (id=group.id, name=group.name.strip())
    print(timeit(lambda:map(clean,db.get_group_list()), number=1))
    #sorted(ui_list, key=Configurations_group.id_or_max) == sorted(db_list, key=Configurations_group.id_or_max)