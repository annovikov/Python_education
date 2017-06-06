# -*- coding: utf-8 -*-
from model.groups import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First test", header="Python group", footer="comment"))
    app.session.logout()
