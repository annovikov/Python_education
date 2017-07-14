from model.contact import ContactGroup
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contactgroup):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contactgroup)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

    def fill_contact_form(self, contactgroup):
        wd = self.app.wd
        self.change_fields("firstname", contactgroup.firstname)
        self.change_fields("lastname", contactgroup.lastname)
        self.change_fields("nickname", contactgroup.nickname)
        self.change_fields("company", contactgroup.company)
        self.change_fields("address", contactgroup.address)
        self.change_fields("home", contactgroup.home)
        self.change_fields("work", contactgroup.work)
        self.change_fields("mobile", contactgroup.mobile)
        self.change_fields("email", contactgroup.email)
        self.change_fields("email2", contactgroup.email2)
        self.change_fields("address2", contactgroup.address2)
        self.change_fields("middlename", contactgroup.middlename)
        self.change_fields("notes", contactgroup.notes)

    def change_fields(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_by_index(self, index, new_contactgroup):
        wd = self.app.wd
        self.open_contacts_page()
        # self.select_contact_by_index(index)
        # search Modify btn with index
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr["+str(index+2)+"]/td[8]/a/img").click()
        self.fill_contact_form(new_contactgroup)
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def modify_by_id(self, id, new_contactgroup):
        wd = self.app.wd
        self.open_contacts_page()
        # self.select_contact_by_index(index)
        # search Modify btn with index
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr["+str(id+2)+"]/td[8]/a/img").click()
        self.fill_contact_form(new_contactgroup)
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def modify_first(self):
        self.modify_by_index(0)


    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")  > 0):
            wd.find_element_by_link_text("home").click()

    def select_add_group_from_list(self, id):
        wd = self.app.wd
        #wd.find_elements_by_xpath(".//*[@id='content']/form[2]/div[4]/select/option")[index2].click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[4]//option[@value='%s']" % id).click()
        wd.find_element_by_name("add").click()

    def select_group_for_deletion(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='right']//option[@value='%s']" % id).click()

    def delete_contact_from_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()



    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group
        self.select_contact_by_index(index)
        # delete
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group
        self.select_contact_by_id(id)
        # delete
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def delete_first(self):
        self.delete_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='%s']" % id).click()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tbody/tr[@name='entry']"):
                firstname = element.find_element_by_xpath("td[3]").text
                lastname = element.find_element_by_xpath("td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_xpath("td[6]").text
                all_emails = element.find_element_by_xpath("td[5]").text
                address = element.find_element_by_xpath("td[4]").text
                self.contact_cash.append(ContactGroup(firstname=firstname, lastname=lastname, id=id, address=address, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cash)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return ContactGroup(firstname=firstname, lastname=lastname, id=id, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                            secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)



    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return ContactGroup(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

