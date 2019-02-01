
# Author: Onuoha Jachimike a.k.a the man of Lightning
# A Handy and secure app for students with links to helpful websites for homework and studying

# Initialize the program
import Tkinter as tk
import ttk
from PIL import ImageTk, Image
import sqlite3
import random
import string
from new_accountclass import new_account, more_info
import tkMessageBox
import datetime
from formulapp import mainapp

# Main page design
win = tk.Tk()
win.title("Raptor Base")
win.resizable(False, False)
win.geometry("610x500")
win.config(background='black')
Greet = ttk.Label(text="Welcome", foreground="green", background='black')
Greet.config(font=10)
Greet.pack(anchor='center')
Filler = ttk.Label(text="To", foreground='green', background='black')
Filler.config(font=10)
Filler.pack(anchor='center')
label_one = ttk.Label(win, text="Raptor Base", foreground='green',
                      background='black')
label_one.config(font=10)
label_one.pack(anchor='center')
UserData = {"Lightning": "123",
            "Thunder": "Kaboom"}
im = Image.open("C:/Users/Jachimike Onuoha/Desktop/work/Scratch.gif")
logo = ImageTk.PhotoImage(im)
panel = ttk.Label(win, width=10, image=logo, background='black')
panel.pack(anchor='center')

# The create account function starts
# Create Account window design starts


def create_account():
        new = tk.Tk()
        new.title('Account creator')
        new.geometry("530x300")
        new.resizable(False, False)
        new.config(background='black')

        L1 = ttk.Label(new, text="First Name", foreground='grey', background='black')
        L1.grid(row=1, column=0, sticky='W')
        L2 = ttk.Label(new, text="Last Name", foreground='grey', background='black')
        L2.grid(row=1, column=3, sticky='E', padx=5)
        L3 = ttk.Label(new, text="Date of Birth", foreground='grey', background='black')
        L3.grid(row=3, column=0, sticky='W')
        L4 = ttk.Label(new, text="School", foreground='grey', background='black')
        L4.grid(row=3, column=3, sticky='E', padx=5)
        L5 = ttk.Label(new, text="Major", foreground='grey', background='black')
        L5.grid(row=5, column=3, sticky='E', padx=5)
        L6 = ttk.Label(new, text="Year", foreground='grey', background='black')
        L6.grid(row=5, column=0, sticky='W')
        L7 = ttk.Label(new, text="Student ID", foreground='grey', background='black')
        L7.grid(row=9, column=3)
        L8 = ttk.Label(new, text="Password", foreground='grey', background='black')
        L8.grid(row=11, column=3)
        L9 = ttk.Label(new, text="Gender", foreground='grey', background='black')
        L9.grid(row=7, column=0, sticky='W')

        Entry1 = ttk.Entry(justify='center')
        Entry1.grid(row=1, column=2, padx=5)
        Entry2 = ttk.Entry(justify='center')
        Entry2.grid(row=1, column=4, sticky='E')
        Entry3 = ttk.Entry(justify='center')
        Entry3.grid(row=3, column=2, padx=5, pady=6)
        Entry4 = ttk.Entry(justify='center')
        Entry4.grid(row=3, column=4, padx=0)
        Entry5 = ttk.Entry(justify='center')
        Entry5.grid(row=5, column=2, padx=0, pady=6)
        Entry6 = ttk.Entry(justify='center')
        Entry6.grid(row=5, column=4, sticky='W')
        Entry7 = ttk.Entry(justify='center')
        Entry7.grid(row=10, column=3, padx=0)
        Entry8 = ttk.Entry(justify='center')
        Entry8.grid(row=12, column=3, padx=0)
        Entry9 = ttk.Combobox(new, values=["Male", "Female", "Other"])
        Entry9.config(width=8)
        Entry9.grid(row=7, column=2, padx=5, pady=6, sticky='W')
# Create account window design ends

        # Default inserts
        Entry1.insert(0, "Jane")
        Entry2.insert(0, "Doe")
        Entry3.insert(0, "MM/DD/YYYY")
        Entry4.insert(0, "University of Lightning")
        Entry5.insert(0, "Freshman")
        Entry6.insert(0, "Medicine")

        # Password generator
        P = random.choice(string.letters)
        A = random.choice(string.letters)
        S = str(random.randint(0, 9))
        W = str(random.randint(0, 9))
        R = str(random.randint(0, 9))
        D = str(random.randint(0, 9))
        code = (P+A+S+W+R+D)
        Entry8.insert(0, code)
        Entry8.config(state='disabled')

        def Create():
            Data = sqlite3.connect("AllUsers")
            c = Data.cursor()

            def insert_user(Pers):
                with Data:
                    c.execute('''INSERT INTO Accounts VALUES(:first, :last, :Birth, :gender, :school, :year, :major)''', {'first': Pers.firstname, 'last': Pers.lastname, 'Birth': Pers.DateOfBirth, 'gender': Pers.Gender, 'school': Pers.School, 'year': Pers.Year, 'major': Pers.Major})

            def update_major(Pers, Major):
                with Data:
                    c.execute('''UPDATE Accounts SET major = :major WHERE first = :first AND last = :last''',
                              {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.Major})

            def update_Year(Pers, Year):
                with Data:
                    c.execute('''UPDATE Accounts SET major = :Year WHERE first = :first AND last = :last''',
                              {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.Year})

            def update_School(Pers, School):
                with Data:
                    c.execute('''UPDATE Accounts SET major = :School WHERE first = :first AND last = :last''',
                              {'first': Pers.firstname, 'last': Pers.lastname, 'major': Pers.School})

            def get_user(lastname):
                c.execute("""SELECT * FROM Accounts WHERE Lastname= :last""", {'last': lastname})
                return c.fetchall()

            # database function end

            # Adds new user to database
            check = Entry7.get()
            if len(check) == 0:
                print("Username cannot be empty")
            else:
                user = new_account(Entry1.get(), Entry2.get(), Entry3.get(), Entry9.get(), Entry4.get(), Entry5.get(), Entry6.get())
                insert_user(user)
                Good = ttk.Label(text='Created! Restart Program', background='black', foreground='green')
                Good.grid(row=14, column=3)

            Data.close()

            # Username and Password Assignment starts

            Log = sqlite3.connect("Users")

            L = Log.cursor()

            '''L.execute("""CREATE TABLE People (Username text, Password blob)""")'''

            '''Log.commit()'''

            def insert_info(Pers):
                with Log:
                    L.execute("INSERT INTO People VALUES(:Username, :Password, :Day, :Month, :Year)",
                              {'Username': Pers.Username, 'Password': Pers.Password, 'Day': Pers.Daymade, 'Month': Pers.Monthmade, 'Year': Pers.Yearmade})

            def get_info_user(Pers):
                L.execute("""SELECT * FROM People WHERE Username = :ident""", {'ident': Pers.Username})

            def del_user(Pers):
                with Log:
                    L.execute("""DELETE FROM People WHERE Username = :them""", {'them': Pers.Username})
            # Username and Password Assignment end
            # Inserts new Username and Password
            now = datetime.datetime.now()
            check = Entry7.get()
            if len(check) == 0:
                tkMessageBox.showerror('Error', "Username Cannot be empty")
            else:
                Stuff = more_info(Entry7.get(), Entry8.get(), now.day, now.month, now.year)
                insert_info(Stuff)
                Create.destroy()

            Log.close()

        Create = ttk.Button(text="Create", command=Create)
        Create.grid(row=13, column=3, pady=15)

        new.mainloop()


# The create account function END

# The sign in function START
# sign in page window design
def sign_in_page():
        log = tk.Tk()
        log.title("Sign In")
        log.geometry("300x150")
        log.resizable(False, False)
        log.config(background='black')

        L1 = ttk.Label(text="Username", foreground='grey', background='black')
        L1.pack(anchor='center')
        Entry1 = ttk.Entry(justify='center')
        Entry1.pack(anchor='center')
        L2 = ttk.Label(text="Password", foreground='grey', background='black')
        L2.pack(anchor='center')
        Entry2 = ttk.Entry(justify='center', show='*')
        Entry2.pack(anchor='center')

        # Sign in Mechanism: Checks username and password database
        def sigin():

            Log = sqlite3.connect("Users")

            L = Log.cursor()

            def insert_info(Pers):
                with Log:
                    L.execute("INSERT INTO People VALUES(:Username, :Password)",
                              {'Username': Pers.Username, 'Password': Pers.Password})

            def get_info_userbyname(Username):
                L.execute("""SELECT * FROM People WHERE Username = :ident""", {'ident': Username})
                return L.fetchall()

            def del_user_by_Username(Username):
                with Log:
                    L.execute("""DELETE FROM People WHERE Username = :them""", {'them': Username})

            def del_user_by_passcode(Password):
                with Log:
                    L.execute("""DELETE FROM People WHERE Password = :them""", {'them': Password})


            # This matches the username and Password
            username = Entry1.get()
            password = Entry2.get()
            with Log:
                L.execute(""" SELECT * FROM People WHERE Username = :name AND Password = :code""", {'name': username, 'code': password})
                results = L.fetchall()
                if results:
                    for i in results:
                        print ("Welcome to Raptor Base")
                        Login.destroy()
                        Back.config(text='OK')
                        Success = ttk.Label(text='Login Successful', background='black', foreground='green')
                        Success.pack(anchor='center')
                        log.destroy()
                        mainapp()
                        break
                else:
                    tkMessageBox.showerror('Error', "User not recognised")

            Log.close()

        Login = ttk.Button(text="Login", command=sigin)
        Login.pack(anchor='center', pady=10)

        def back():
            log.destroy()

        Back = ttk.Button(text='Cancel', command=back)
        Back.pack(anchor='center', pady=1)

        log.mainloop()
# The sign in function END

# Create Account functon call


def clicky():
    win.destroy()
    create_account()

# Sign in function call


def press():
    win.destroy()
    sign_in_page()


# Create Account Button
action = ttk.Button(win, text="Create Account", command=clicky)
action.pack(anchor='center', pady=5)

# Sign in Button
tap = ttk.Button(win, text="Sign In", command=press)

tap.pack(anchor='center', pady=5)

win.mainloop()
