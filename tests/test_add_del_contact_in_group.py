from model.contact import ContactGroup
import random
from fixture.orm import ORMFixture
from model.groups import Group
import time



def test_add_contact_to_group(app, db):
    #if app.contact.count() == 0:
       # app.contact.add_new(ContactGroup(firstname="test9", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru", address2="Lenina str 5/7"))
    list_contacts = db.get_contact_list()
    list_groups = db.get_group_list()
    contact = random.choice(list_contacts)
    group = random.choice(list_groups)
    print(group)
    db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    app.contact.open_contacts_page()
    app.contact.select_contact_by_id(contact.id)
    app.contact.select_add_group_from_list(group.id)
    time.sleep(3)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    for item in new_contacts_in_group:
        print(item)
    print(len(new_contacts_in_group))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=ContactGroup.id_or_max) == sorted(new_contacts_in_group, key=ContactGroup.id_or_max)
    # now try to delete contact from group
    app.contact.open_contacts_page()
    app.contact.select_group_for_deletion(group.id)
    app.contact.select_contact_by_id(contact.id)
    app.contact.delete_contact_from_group()
    time.sleep(3)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=ContactGroup.id_or_max) == sorted(new_contacts_in_group,
                                                                               key=ContactGroup.id_or_max)

