from sys import maxsize
class Configurations_user:
    def __init__(self, firstname=None, middlename=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 phone_home=None,phone_mobile=None, phone_work=None, mail1=None, mail2=None, mail3=None, bd_day=None, bd_month=None,
                 bd_year=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, user_name=None, all_mail=None):
        self.firstname = firstname
        self.middlename = middlename
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.bd_day = bd_day
        self.bd_month = bd_month
        self.bd_year = bd_year
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.user_name= user_name
        self.all_mail = all_mail

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
                and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize