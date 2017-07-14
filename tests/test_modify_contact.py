# -*- coding: utf-8 -*-
from model.contact import ContactGroup
from random import randrange
import random

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = ContactGroup(address="Ufa", address2="1905 str 5/7",middlename="Ivanovich", notes="modified")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)


def test_modify_some_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data = ContactGroup(address="Ufa", address2="1905 str 5/7",middlename="Ivanovich", notes="modified")
    contact_data.id = old_contacts[id].id
    contact_data.lastname = old_contacts[id].lastname
    contact_data.firstname = old_contacts[id].firstname
    app.contact.modify_by_id(id, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactGroup.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactGroup.id_or_max)


