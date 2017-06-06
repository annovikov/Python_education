# -*- coding: utf-8 -*-
from model.groups import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="Modified test", header="Python group", footer="comment"))
    app.session.logout()

