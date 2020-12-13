from model.configurations_group import Configurations_group
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean (group):
        return Configurations_group (id=group.id, name=group.name.strip())
    db_list = map(clean,db.get_group_list())
    assert sorted(ui_list, key=Configurations_group.id_or_max) == sorted(db_list, key=Configurations_group.id_or_max)