# Homework help websites
import Tkinter as tk
import ttk
import webbrowser
import tkFont


# Homework help main window design
def mainapp():
    form = tk.Tk()
    form.title("Raptorapp")
    form.geometry("300x320")
    form.config(background='black')
    form.resizable(False, False)

    Label = ttk.Label(text="Pick a topic to get help", foreground='black', background='green', font='system')
    Label.pack(anchor='center')

    # Calculus site
    def Calc():
        webbrowser.open('http://tutorial.math.lamar.edu/')
        webbrowser.open('https://www.symbolab.com/')

        # Physics site
    def Phys():
        webbrowser.open('http://www.feynmanlectures.caltech.edu/')

        # Chemistry site
    def Chem():
        webbrowser.open('https://cnx.org/contents/havxkyvS@12.1:b39avmGq@34/Preface')

        # Biology site
    def Bio():
        webbrowser.open('https://bio.libretexts.org/')

        # Economics site
    def Econ():
        webbrowser.open('http://www.acdcecon.com/')

        # Extra help sites
    def GetHelp():
        webbrowser.open('https://www.youtube.com/user/crashcourse')
        webbrowser.open('https://www.chegg.com/')

        # GUI design
    Calculus = ttk.Button(form, text="Calculus", command=Calc, width=30)
    Calculus.pack(anchor='center', pady=10)
    Physics = ttk.Button(text="Physics", command=Phys, width=30)
    Physics.pack(anchor='center', pady=10)
    Chemistry = ttk.Button(text="Chemistry", command=Chem, width=30)
    Chemistry.pack(anchor='center', pady=10)
    Biology = ttk.Button(text="Biology", command=Bio, width=30)
    Biology.pack(anchor='center', pady=10)
    Economics = ttk.Button(text="Economics", command=Econ, width=30)
    Economics.pack(anchor='center', pady=10)
    Label1 = ttk.Label(text="Still Lost?", foreground='black', background='green', font='system')
    Label1.pack(anchor='center')
    GetHelp = ttk.Button(form, text='Get Help', command=GetHelp, width=10)
    GetHelp.pack(anchor='center', pady=15)
    form.mainloop()
