import sqlite3
import pandas as pd
from more_infoclass import more_info

# creates the database
Log = sqlite3.connect("Users")

L = Log.cursor()
# Uncomment  this to create the SQL table, then re-comment it
'''L.execute("""CREATE TABLE People (Username text, Password blob, Day integer, Month integer, Year integer)""")

Log.commit()'''


# insert new user
def insert_info(Pers):
    with Log:
        L.execute("INSERT INTO People VALUES(:Username, :Password)",
                  {'Username': Pers.Username, 'Password': Pers.Password})


# get user data by ther username
def get_info_userbyname(Username):
    L.execute("""SELECT * FROM People WHERE Username = :ident""", {'ident': Username})
    return L.fetchall()


# delete a username by their username
def del_user_by_Username(Username):
    with Log:
        L.execute("""DELETE FROM People WHERE Username = :them""", {'them': Username})


# delete a user by their password
def del_user_by_passcode(Password):
    with Log:
        L.execute("""DELETE FROM People WHERE Password = :them""", {'them': Password})


# Print out database using pandas
print pd.read_sql_query("""SELECT * FROM People""", Log)

Log.close()
