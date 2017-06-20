# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="test9", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
