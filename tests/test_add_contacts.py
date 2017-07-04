# -*- coding: utf-8 -*-
from model.contact import ContactGroup
import pytest
#from data.contacts import testdata
from data.contacts import constant as testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)



def test_add_defined_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactGroup(firstname="test6", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)


