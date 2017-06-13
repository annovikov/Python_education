# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_modify_first_contact(app):

    app.contact.modify_first(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru",
                                     address2="Lenina str 5/7",middlename="Ivanovich", hometel="333333", notes="modified"))
