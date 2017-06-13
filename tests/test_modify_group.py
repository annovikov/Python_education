# -*- coding: utf-8 -*-
from model.groups import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test9", header="Python group", footer="comment"))
    app.group.modify_first(Group(name="Modified test", header="Python group", footer="comment"))


