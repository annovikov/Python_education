# -*- coding: utf-8 -*-
from model.groups import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test9", header="Python group", footer="comment"))
    app.group.delete_first()
