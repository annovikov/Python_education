# -*- coding: utf-8 -*-
from model.groups import Group
from random import randrange
import random

def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test9", header="Python group", footer="comment"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Modified name")
    group.id = old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_some_group_db(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test9", header="Python group", footer="comment"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    newdata = Group(name="Modified name")
    app.group.modify_by_id(group.id, newdata)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    print(old_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    #old_groups.remove(group)
    #old_groups[2].insert(3,'name')
    #old_groups.append(int(group.id), group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



