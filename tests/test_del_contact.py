# -*- coding: utf-8 -*-
from model.contact import ContactGroup
from random import randrange
import random
import time

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="test9", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="test9", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

def test_delete_some_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(ContactGroup(firstname="test9", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    time.sleep(4)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=ContactGroup.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactGroup.id_or_max)
