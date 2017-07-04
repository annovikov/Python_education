from model.contact import ContactGroup
import random
import string
import json
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o =="-f":
        f=a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix +"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [ContactGroup(firstname="", lastname="", middlename="", company="TTY", address="Ekaterinburg", home="", work="", mobile="", email="")] + [
    ContactGroup(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), middlename=random_string("middlename", 10), company=random_string("company", 20),
                 address=random_string("address", 30), home=random_string("home", 10), work=random_string("work", 10), mobile=random_string("mobile", 10),
                 email=random_string("email", 10), email2=random_string("email2", 10))
    for i in range(n)
]

file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))