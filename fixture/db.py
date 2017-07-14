import mysql.connector
from model.groups import Group
from model.contact import ContactGroup

class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit=True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list ")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, address, home, work, mobile, "
                           "email, email2, address2, notes  from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, address, home, work, mobile,
                 email, email2, address2, notes) = row
               # if deprecated is '0000-00-00 00:00:00':
                list.append(ContactGroup(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                         company=company, address=address, home=home, work=work, mobile=mobile, email=email, email2=email2, address2=address2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()