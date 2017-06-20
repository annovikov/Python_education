# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_add_contacts(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactGroup(firstname="test6", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)


