from random import randrange
import re

def test_all_data_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
   # assert contact_from_home_page.address == merge_address_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",                                # 4-склеиваем с помощью перевода строки, 3-выкидываются пустые строки,
                     map(lambda x: clear(x),                                  # 2-отчищаем от лишних символов,
                         filter(lambda x: x is not None,                       # 1-выкидываем из списка пустые значения,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",                                # 4-склеиваем с помощью перевода строки, 3-выкидываются пустые строки,
                     map(lambda x: clear(x),                                  # 2-отчищаем от лишних символов,
                         filter(lambda x: x is not None,                       # 1-выкидываем из списка пустые значения,
                                [contact.email, contact.email2, contact.email3]))))

def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",                                # 4-склеиваем с помощью перевода строки, 3-выкидываются пустые строки,
                     map(lambda x: clear(x),                                  # 2-отчищаем от лишних символов,
                         filter(lambda x: x is not None,                       # 1-выкидываем из списка пустые значения,
                                [contact.address]))))


