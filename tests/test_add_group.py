# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.groups import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="First test", header="Python group", footer="comment"))
    app.logout()