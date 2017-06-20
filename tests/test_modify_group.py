# -*- coding: utf-8 -*-
from model.groups import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test9", header="Python group", footer="comment"))
    old_groups = app.group.get_group_list()
    group = Group(name="Modified name")
    group.id = old_groups[0].id
    app.group.modify_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




