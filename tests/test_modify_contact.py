# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg",
                            hometel="55557777", email="fakemail@ty.ru",
                            address2="Lenina str 5/7", middlename="", notes=""))
    app.contact.modify_first(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", email="fakemail@ty.ru",
                                          address2="Lenina str 5/7",middlename="Ivanovich", hometel="333333", notes="modified"))
