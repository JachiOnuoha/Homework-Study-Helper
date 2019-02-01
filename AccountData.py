import sqlite3
import pandas as pd
from new_accountclass import new_account

# creates the database
Data = sqlite3.connect("AllUsers")
c = Data.cursor()

# Uncomment this to create the SQL table, then re-comment it
'''c.execute("""CREATE TABLE Accounts (Firstname text, Lastname text, DateOfBirth blob,
                                    Gender text, School text, Year text, Major text)""")

Data.commit()'''


# Manually insert a user
def insert_user(Pers):
    with Data:
        c.execute('''INSERT INTO Accounts VALUES(:first, :last, :Birth, :gender, :school, :year, :major)''', {'first': Pers.firstname, 'last': Pers.lastname, 'Birth': Pers.DateOfBirth, 'gender': Pers.Gender, 'school': Pers.School, 'year': Pers.Year, 'major': Pers.Major})


# Update a user's major
def update_major(Pers, Major):
    with Data:
        c.execute('''UPDATE Accounts SET major = :major WHERE first = :first AND last = :last''',
                  {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.Major})


# Update a user's school year
def update_Year(Pers, Year):
    with Data:
        c.execute('''UPDATE Accounts SET major = :Year WHERE first = :first AND last = :last''',
                  {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.Year})


# Update a user's school
def update_School(Pers, School):
    with Data:
        c.execute('''UPDATE Accounts SET major = :School WHERE first = :first AND last = :last''',
                  {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.School})


# Get a user by their name
def get_user_by_name(firstname, lastname):
    c.execute("""SELECT * FROM Accounts WHERE Firstname= :first AND Lastname= :last""", {'first': firstname, 'last': lastname})
    return c.fetchall()


# Delete a user by their name
def del_user_by_name(firstname, lastname):
    with Data:
        c.execute("""DELETE FROM Accounts WHERE  Firstname= :first AND Lastname= :last""", {'first': firstname, 'last': lastname})


# Prints out the whole database using pandas
print pd.read_sql_query("""SELECT * FROM Accounts""", Data)
Data.close()
