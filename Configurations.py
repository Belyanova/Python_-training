class Configurations_login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Configurations_group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Configurations_user:
    def __init__(self, firstname, middlename, last_name, nickname, title, company, address, phone_home,
                     phone_mobile, phone_work, mail1, mail2, mail3, bd_day, bd_month, bd_year, aday, amonth, ayear,
                     address2, phone2, notes):
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