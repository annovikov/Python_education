# -*- coding: utf-8 -*-
from model.contact import ContactGroup
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix +"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [ContactGroup(firstname="", lastname="", middlename="", company="TTY", address="Ekaterinburg", home="", work="", mobile="", email="")] + [
    ContactGroup(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), middlename=random_string("middlename", 10), company=random_string("company", 20),
                 address=random_string("address", 30), home=random_string("home", 10), work=random_string("work", 10), mobile=random_string("mobile", 10),
                 email=random_string("email", 10), email2=random_string("email2", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)



def test_add_define_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactGroup(firstname="test6", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactGroup.id_or_max) == sorted(new_contacts, key=ContactGroup.id_or_max)


