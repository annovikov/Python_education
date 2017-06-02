# -*- coding: utf-8 -*-
import pytest
from contact import ContactGroup
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contacts(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", hometel="55557777", email="fakemail@ty.ru",
                            address2="Lenina str 5/7"))
    app.logout()

