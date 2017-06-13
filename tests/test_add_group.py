# -*- coding: utf-8 -*-
from model.groups import Group


def test_add_group(app):

    app.group.create(Group(name="First test", header="Python group", footer="comment"))

