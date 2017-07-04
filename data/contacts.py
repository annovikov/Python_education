from model.contact import ContactGroup
import random
import string

constant = [
    ContactGroup(firstname="firstname1", lastname="lastname1", middlename="middlename1", company="company1", address="address1", home="home1", work="work1", mobile="mobile1", email="email"),
    ContactGroup(firstname="firstname2", lastname="lastname2", middlename="middlename2", company="company2", address="address2", home="home2", work="work2", mobile="mobile2", email="emai2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix +"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [ContactGroup(firstname="", lastname="", middlename="", company="TTY", address="Ekaterinburg", home="", work="", mobile="", email="")] + [
    ContactGroup(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), middlename=random_string("middlename", 10), company=random_string("company", 20),
                 address=random_string("address", 30), home=random_string("home", 10), work=random_string("work", 10), mobile=random_string("mobile", 10),
                 email=random_string("email", 10), email2=random_string("email2", 10))
    for i in range(5)
]