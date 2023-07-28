from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Attendance")

#registration and login form
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
#for attendance form
STUDENTNAME = StringVar()
REGNO = StringVar()
var = StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member3.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'member' (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT, password TEXT,firstname TEXT, lastname TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'students' (stud_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Studentname TEXT, regno TEXT,var TEXT)")

def Exit():
    result = tkMessageBox.askquestion('System','Are you sure you want to exit?', icon = "warning")
    if result == 'yes':
        root.destroy()
        exit()

def LoginForm():
    root.geometry("600x400")  # w X h
    global LoginFrame, label_result1
    LoginFrame = Frame(root)
    LoginFrame.pack()

    title = Label(LoginFrame,text = 'Login Form',fg = 'red',font = ('arial 30 bold'),bd=18)
    title.grid(row=0,pady=20)
    label_username = Label(LoginFrame,text='Username:',font=('arial',25),bd=18)
    label_username.grid(row=1)
    label_password = Label(LoginFrame,text='Password:',font=('arial',25),bd=18)
    label_password.grid(row=2)
    label_result1 = Label(LoginFrame, text ="", font = ('arial', 18))
    label_result1.grid(row=3, columnspan = 2)

    username = Entry(LoginFrame,font = ('arial',20),textvariable=USERNAME,width=15)
    username.grid(row=1,column=1)
    password = Entry(LoginFrame,font = ('arial',20),textvariable=PASSWORD,width=15,show="*")
    password.grid(row=2,column=1)
    btn_login = Button(LoginFrame,text="login",font = ('arial',18),width = 35,command = Login)
    btn_login.grid(row=5,columnspan = 2,pady = 20)

    label_register = Label(LoginFrame,text = "CREATE ACCOUNT",fg = "blue",font = ('arial',18))
    label_register.grid(row = 4, sticky=W)
    label_register.bind('<Button-1>', ToggleToRegister)

def RegistrationForm():
    root.geometry("900x650")  # w X h
    global RegistrationFrame,label_result2
    RegistrationFrame = Frame(root)
    RegistrationFrame.pack(side = TOP, pady = 40)
    title1 = Label(RegistrationFrame, text ='Registration Form', fg ='red', font = ('arial 25 bold'), bd=18)
    title1.grid(row=0)
    Regis_label_Username = Label(RegistrationFrame, text='Username:', font=('arial', 25), bd=18)
    Regis_label_Username.grid(row=1)
    Regis_label_password = Label(RegistrationFrame, text='Password:', font=('arial', 25), bd=18)
    Regis_label_password.grid(row=2)
    Regis_label_firstname = Label(RegistrationFrame, text='First Name:', font=('arial', 25), bd=18)
    Regis_label_firstname.grid(row=3)
    Regis_label_lastname = Label(RegistrationFrame, text='Last Name:', font=('arial', 25), bd=18)
    Regis_label_lastname.grid(row=4)
    label_result2 = Label(RegistrationFrame, text ="", font = ('arial', 18))
    label_result2.grid(row=5, columnspan = 2)
    username = Entry(RegistrationFrame, font = ('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1,column=1)
    password = Entry(RegistrationFrame, font = ('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2,column=1)
    firstname = Entry(RegistrationFrame, font = ('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3,column=1)
    lastname = Entry(RegistrationFrame, font = ('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4,column=1)

    btn_login = Button(RegistrationFrame, text="Register", font = ('arial', 18), width = 35, command = Register)
    btn_login.grid(row=6,columnspan = 2,pady = 20)
    label_login = Label(RegistrationFrame, text ="GO TO LOGIN FROM", fg ="blue", font = ('arial', 15))
    label_login.grid(row = 7,sticky = W)
    label_login.bind('<Button-1>', ToggleToLogin)

def AttendanceForm():
    root.geometry("900x700")  # w X h
    # global AttendanceForm, label_result3
    global AttendanceFrame, label_result3
    AttendanceFrame = Frame(root)
    AttendanceFrame.pack(side = TOP, pady = 20)
    title2 = Label(AttendanceFrame, text ='Online Attendance', fg ='red', font = ('arial 25 bold'), bd=18)
    title2.grid(row=0)
    lb1_studentname = Label(AttendanceFrame, text='Student name:', font=('arial', 25), bd=18)
    lb1_studentname.grid(row=1)
    lb1_regno = Label(AttendanceFrame, text='Reg No:', font=('arial', 25), bd=18)
    lb1_regno.grid(row=2)

    label_3 = Label(AttendanceFrame, text ="STATUS", width=20, font = ('arial', 20))
    label_3.grid(row=4,column=0)

    label_result3 = Label(AttendanceFrame, text ="", font = ('arial', 18))
    label_result3.grid(row=5, columnspan = 2)
    studentname = Entry(AttendanceFrame, font = ('arial', 20), textvariable=STUDENTNAME, width=15)
    studentname.grid(row=1,column=1)
    regno = Entry(AttendanceFrame, font = ('arial', 20), textvariable=REGNO, width=15)
    regno.grid(row=2,column=1)

    present = Radiobutton(AttendanceFrame, text ="present", padx=5, variable=var, value="P")
    present.grid(row=4,column=1)
    present = Radiobutton(AttendanceFrame, text ="absent", padx=20, variable=var, value="A")
    present.grid(row=4,column=2)

    btn_submit = Button(AttendanceFrame, text="SUBMIT", font = ('arial', 18), width = 35, command = Submit)
    btn_submit.grid(row=6,columnspan = 2,pady = 20)

    label_login = Label(AttendanceFrame, text="GO TO LOGIN FROM", fg="blue", font=('arial', 15))
    label_login.grid(row=7, sticky=W)
    label_login.bind('<Button-1>', ToggleFromAttendanceToLogin)

def ToggleToLogin(event = None):
    RegistrationFrame.destroy()
    LoginForm()

def ToggleToRegister(event = None):
    LoginFrame.destroy()
    RegistrationForm()

def ToggleToSubmit(event = None):
    LoginFrame.destroy()
    AttendanceForm()
def ToggleFromAttendanceToLogin(event = None):
    AttendanceFrame.destroy()
    LoginForm()

def Register():
    Database()
    if (USERNAME.get()=="") or (PASSWORD.get()=="")  or (FIRSTNAME.get()=="") or (LASTNAME.get()==""):
        label_result2.config(text ="KINDLY COMPLETE THE REQUIRED FIELD", fg="orange")
    else:
        cursor.execute('SELECT * FROM member WHERE username=?',(USERNAME.get(),))
        if cursor.fetchone() is not None:
            label_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute('INSERT INTO member (username, password, firstname, lastname) VALUES (?, ?, ?, ?)',(str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            label_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()

def Login():
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            label_result1.config(text="PLEASE COMPLETE THE REQUIRED FIELD", fg="orange")
        else:
            cursor.execute('SELECT * FROM member WHERE username=? and password=?', (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                ToggleToSubmit()
            else:
                label_result1.config(text="Invalid Username or Password", fg="red")

def Submit():
    Database()
    if STUDENTNAME.get == "" or REGNO.get() == "" or var.get() == "":
        label_result3.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM 'students' WHERE 'studentname' = ?", (STUDENTNAME.get(),))
        if cursor.fetchone() is not None:
            label_result3.config(text="Studentname is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO 'students' (studentname, regno ,var) VALUES(?, ?, ?)", (str(STUDENTNAME.get()), str(REGNO.get()), str(var.get())))
            conn.commit()
            STUDENTNAME.set("")
            REGNO.set("")
            var.set("")
            def View():
                conn = sqlite3.connect("db_member3.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM students")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                    tree.insert("",tk.END,values=row)
                conn.close()

            tree = ttk.Treeview(AttendanceFrame, column=("column1", "column2", "column3", "column4"), show='headings')
            tree.heading("#1", text="stud_no")
            tree.heading("#2", text="Studentname")
            tree.heading("#3", text="regno")
            tree.heading("#4", text="status")
            tree.grid(row=10,columnspan =6)

            b2 = tk.Button(AttendanceFrame,text="view data", command=View)
            b2.grid(row=15,column=1)

        cursor.close()
        conn.close()

LoginForm()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu = menubar)

if __name__ == '__main__':
    root.mainloop()
