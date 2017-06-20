from model.contact import ContactGroup

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
        self.change_fields("email", contactgroup.email)
        self.change_fields("address2", contactgroup.address2)
        self.change_fields("middlename", contactgroup.middlename)
        self.change_fields("notes", contactgroup.notes)

    def change_fields(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first(self, new_contactgroup):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contactgroup)
        wd.find_element_by_name("update").click()
        self.contact_cash = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

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
                self.contact_cash.append(ContactGroup(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cash)




