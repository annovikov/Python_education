# -*- coding: utf-8 -*-
from model.groups import Group
from random import randrange
import random
import pytest

def test_delete_first_group(app):
    with pytest.allure.step('Create new group if list is empty'):
        if app.group.count() == 0:
           app.group.create(Group(name="test9", header="Python group", footer="comment"))
    with pytest.allure.step('Given a group list'):
        old_groups = app.group.get_group_list()
    with pytest.allure.step('Delete first group'):
        app.group.delete_first()
    with pytest.allure.step('The new group list is equal to the old list with deleted group'):
        new_groups = app.group.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups[0:1] = []
        assert old_groups == new_groups


def test_delete_some_group(app):
    with pytest.allure.step('Create new group if list is empty'):
        if app.group.count() == 0:
           app.group.create(Group(name="test9", header="Python group", footer="comment"))
    with pytest.allure.step('Given a group list'):
        old_groups = app.group.get_group_list()
    with pytest.allure.step('Get a index of group'):
        index = randrange(len(old_groups))
    with pytest.allure.step('Delete group with index %s' % index):
        app.group.delete_by_index(index)
    with pytest.allure.step('The new group list is equal to the old list with deleted group'):
        new_groups = app.group.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups[index:index+1] = []
        assert old_groups == new_groups


def test_delete_some_group_db(app, db, check_ui):
    with pytest.allure.step('Create new group if list is empty'):
        if len(db.get_group_list()) == 0:
           app.group.create(Group(name="test9", header="Python group", footer="comment"))
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Get a id of group'):
        group = random.choice(old_groups)
    with pytest.allure.step('Delete group with group id %s' % group.id):
        app.group.delete_by_id(group.id)
    with pytest.allure.step('The new group list is equal to the old list with deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
           assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)