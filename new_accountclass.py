import datetime


class new_account():
    def __init__(self, firstname, lastname, DateOfBirth, Gender, School, Year, Major):
        self.firstname = firstname
        self.lastname = lastname
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.School = School
        self.Major = Major
        self.Year = Year


def first_change(user, fname):
    user.firstname = fname


def last_change(user, lname):
    user.lastname = lname


def Birth_change(user, DoB):
    user.DateOfBirth = DoB


def gender_change(user, gend):
    user.Gender = gend


def School_change(user, Sch):
    user.School = Sch


def Major_change(user, Maj):
    user.Major = Maj


# adds time the accout was made
now = datetime.datetime.now()


class more_info():
    def __init__(self, Username, Password, Daymade, Monthmade, Yearmade):
        self.Username = Username
        self.Password = Password
        self.Daymade = Daymade
        self.Monthmade = Monthmade
        self.Yearmade = Yearmade


user = more_info('jon226', 1234, now.day, now.month, now.year)
