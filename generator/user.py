from model.configurations_user import Configurations_user
import random
import string
import os.path
import jsonpickle
import getopt
import sys
from random import randint

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



def random_month():
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return random.choice(month)

testdata = [
    Configurations_user(firstname=random_string("firstname", 3), middlename=random_string("middlename", 5),
                        last_name=random_string("last_name", 3), nickname=random_string("nickname", 5),
                        title=random_string("title", 3), company=random_string("company", 5),
                        address=random_string("address", 3), phone_home=random_string("phone_home", 5),
                        phone_mobile=random_string("phone_mobile", 3), phone_work=random_string("phone_work", 5),
                        mail1=random_string("mail1", 3), mail2=random_string("mail2", 5),mail3=random_string("mail3", 3),
                        bd_day=str(randint(1, 31)), bd_month=random_month(),bd_year=str(randint(1900, 2100)),
                        aday=str(randint(1, 31)),amonth=random_month(),ayear=(randint(1900, 2100)),
                        address2=random_string("address2", 5), phone2=random_string("phone2", 3),notes = random_string("notes", 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))