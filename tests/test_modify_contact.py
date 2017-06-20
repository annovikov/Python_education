# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactGroup(address="Ufa", address2="1905 str 5/7",middlename="Ivanovich", notes="modified")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    contact.firstname = old_contacts[0].firstname
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)
