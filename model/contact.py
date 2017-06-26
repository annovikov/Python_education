from sys import maxsize

class ContactGroup:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, address=None, email=None, email2=None, email3=None, address2=None, middlename=None, notes=None, id=None,
                 home=None, mobile=None, work=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.middlename = middlename
        self.notes = notes
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname )

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(ct):
        if ct.id:
            return int(ct.id)
        else:
            return maxsize