# -*- coding: utf-8 -*-
from model.contact import ContactGroup

def test_add_contacts(app):

    app.contact.add_new(ContactGroup(firstname="Ivan", lastname="Ivanov", nickname="goodman", company="TTY", address="Ekaterinburg", hometel="55557777", email="fakemail@ty.ru",
                                     address2="Lenina str 5/7", middlename="", notes=""))


