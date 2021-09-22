import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.constants import TRUE
import tkinter.messagebox as messagebox
from tkscrolledframe import ScrolledFrame

import mysql.connector
import re
from setup import init_mysql
from pymongo import MongoClient

    
def LandingPage(root):
    main_screen = root   
    main_screen.title("OSHES app")
    main_screen.config(bg='#0B5A81') 
    main_screen.grid()
 
    tkinter.Label(text="Welcome to OSHES :)", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#0B5A81').pack() 
    tkinter.Button(text="Customer Registration", height="2", width="30", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("registerCustomer")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack() 
    tkinter.Button(text="Customer Login", height="2", width="30", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("loginCustomer")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack() 
    tkinter.Button(text="Admin Registration", height="2", width="30", relief=tkinter.SOLID,cursor='hand2', command= lambda: changepage("registerAdmin")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack() 
    tkinter.Button(text="Admin Login", height="2", width="30", relief=tkinter.SOLID,cursor='hand2', command= lambda: changepage("loginAdmin")).pack()
    
    return 

def AdminSignUpPage(root, cursor, db): 
    def validate_signup_admin():
        check_counter=0
        warn = ""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        insert_statement = "INSERT INTO Administrator (adminName, gender, phoneNumber, adminPassword) VALUES (%s, %s, %s, %s)"
        if register_name.get() == "":
            warn += "\n"
            warn += "Name cannot be empty!"
        else:
            check_counter += 1

        if register_email.get() == "":
            warn += "\n"
            warn += "Email cannot be empty!"
        else:
            check_counter += 1
        if (not re.fullmatch(regex, register_email.get())):
            warn += "\n"
            warn += "Please enter a valid email address!"
        else:
            check_counter += 1
        if register_mobile.get() == "":
            warn += "\n"
            warn += "Phone number cannot be empty!"
        else:
            check_counter += 1
        if ((len(register_mobile.get()) != 8) or (not register_mobile.get().isdigit())):
            print(len(register_mobile.get()))
            warn += "\n"
            warn += "Please enter a valid mobile number! (8 digits)"
        else:
            check_counter += 1  
        if  var.get() == "":
            warn += "\n"        
            warn += "Select Gender"
        else:
            check_counter += 1

        if register_pwd.get() == "":
            warn += "\n"
            warn += "Password cannot be empty!"
        else:
            check_counter += 1

        if pwd_again.get() == "":
            warn += "\n"
            warn += "Re-enter password cannot be empty!"
        else:
            check_counter += 1
        if pwd_again.get() != register_pwd.get():
            warn += "\n"
            warn += "Passwords not matching!"
        else:
            check_counter += 1
        if check_counter == 9:
            try:
                cursor.execute(insert_statement,(register_name.get(), var.get(), register_mobile.get(), register_pwd.get()))
                db.commit()
                messagebox.showinfo('Confirmation', 'You have successfully registered! Please go back to the main page to Log in as an Administrator!')
            except Exception as e:
                messagebox.showerror('', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Administrator Registration')
    ws.config(bg='red')
    f = ('Times', 14)
    var = tkinter.StringVar()
    var.set('Male')

    right_frame = tkinter.Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',
        relief=tkinter.SOLID, 
        padx=10, 
        pady=10
        )

    tkinter.Label(
        right_frame, 
        text="Enter Name", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Email", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Phone Number", 
        bg='#CCCCCC',
        font=f
        ).grid(row=2, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Select Gender", 
        bg='#CCCCCC',
        font=f
        ).grid(row=3, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=4, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Re-Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, sticky=tkinter.W, pady=10)

    gender_frame = tkinter.LabelFrame(
        right_frame,
        bg='#CCCCCC',
        padx=10, 
        pady=10,
        )

    register_name = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_email = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_mobile = tkinter.Entry(
        right_frame, 
        font=f
        )

    male_rb = tkinter.Radiobutton(
        gender_frame, 
        text='Male',
        bg='#CCCCCC',
        variable=var,
        value='Male',
        font=('Times', 10),
    )

    female_rb = tkinter.Radiobutton(
        gender_frame,
        text='Female',
        bg='#CCCCCC',
        variable=var,
        value='Female',
        font=('Times', 10),
    )

    others_rb = tkinter.Radiobutton(
        gender_frame,
        text='Other',
        bg='#CCCCCC',
        variable=var,
        value='Other',
        font=('Times', 10)
    )

    register_pwd = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )
    pwd_again = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )

    register_btn = tkinter.Button(
        right_frame, 
        width=15, 
        text='Register', 
        font=f, 
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_signup_admin
    )

    tkinter.Label(text="Welcome New Admin! :)", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='red').pack()
    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_pwd.grid(row=4, column=1, pady=10, padx=20)
    pwd_again.grid(row=5, column=1, pady=10, padx=20)
    register_btn.grid(row=6, column=1, pady=10, padx=20)
    right_frame.pack()
    gender_frame.grid(row=3, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=tkinter.LEFT)
    female_rb.pack(expand=True, side=tkinter.LEFT)
    others_rb.pack(expand=True, side=tkinter.LEFT)
    tkinter.Button(text="Back to Home", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return 

def CustomerSignUpPage(root, cursor, db):
    def validate_signup():
        check_counter=0
        warn = ""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        insert_statement = "INSERT INTO Customer (customerName, customerPassword, phoneNumber, gender, address, email) VALUES (%s, %s, %s, %s, %s, %s)"
        if register_name.get() == "":
            warn += "\n"
            warn += "Name cannot be empty!"
        else:
            check_counter += 1
        check_counter=0
                
        if register_email.get() == "":
            warn += "\n"
            warn += "Email cannot be empty!"
        else:
            check_counter += 1
        if (not re.fullmatch(regex, register_email.get())):
            warn += "\n"
            warn += "Please enter a valid email address!"
        else:
            check_counter += 1
        if register_mobile.get() == "":
            warn += "\n"
            warn += "Phone number cannot be empty!"
        else:
            check_counter += 1
        if ((len(register_mobile.get()) != 8) or (not register_mobile.get().isdigit())):
            print(len(register_mobile.get()))
            warn += "\n"
            warn += "Please enter a valid mobile number! (8 digits)"
        else:
            check_counter += 1 
        if register_address.get() == "":
            warn += "\n"
            warn += "Address cannot be empty!"
        else:
            check_counter += 1        
        if  var.get() == "":
            warn += "\n"        
            warn += "Select Gender"
        else:
            check_counter += 1

        if register_pwd.get() == "":
            warn += "\n"
            warn += "Password cannot be empty!"
        else:
            check_counter += 1

        if pwd_again.get() == "":
            warn += "\n"
            warn += "Re-enter password cannot be empty!"
        else:
            check_counter += 1
        if pwd_again.get() != register_pwd.get():
            warn += "\n"
            warn += "Passwords not matching!"
        else:
            check_counter += 1
        if check_counter == 9:
            try:
                cursor.execute(insert_statement,(register_name.get(), register_pwd.get(), register_mobile.get(), var.get(), register_address.get(), register_email.get()))
                db.commit()
                messagebox.showinfo('Confirmation', 'You have successfully registered! Please go back to the main page to Log in as a Customer!')
            except Exception as e:
                messagebox.showerror('', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Customer Registration')
    ws.config(bg='#0B5A81')
    f = ('Times', 14)
    var = tkinter.StringVar()
    var.set('Male')

    right_frame = tkinter.Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',
        relief=tkinter.SOLID, 
        padx=10, 
        pady=10
        )

    tkinter.Label(
        right_frame, 
        text="Enter Name", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Email", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Phone Number", 
        bg='#CCCCCC',
        font=f
        ).grid(row=2, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Address", 
        bg='#CCCCCC',
        font=f
        ).grid(row=3, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Select Gender", 
        bg='#CCCCCC',
        font=f
        ).grid(row=4, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Re-Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=6, column=0, sticky=tkinter.W, pady=10)

    gender_frame = tkinter.LabelFrame(
        right_frame,
        bg='#CCCCCC',
        padx=10, 
        pady=10,
        )

    register_name = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_email = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_mobile = tkinter.Entry(
        right_frame, 
        font=f
        )
    
    register_address = tkinter.Entry(
        right_frame, 
        font=f
        )


    male_rb = tkinter.Radiobutton(
        gender_frame, 
        text='Male',
        bg='#CCCCCC',
        variable=var,
        value='Male',
        font=('Times', 10),
        
    )

    female_rb = tkinter.Radiobutton(
        gender_frame,
        text='Female',
        bg='#CCCCCC',
        variable=var,
        value='Female',
        font=('Times', 10),
    
    )

    others_rb = tkinter.Radiobutton(
        gender_frame,
        text='Other',
        bg='#CCCCCC',
        variable=var,
        value='Other',
        font=('Times', 10)
    
    )

    register_pwd = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )
    pwd_again = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )

    register_btn = tkinter.Button(
        right_frame, 
        width=15, 
        text='Register', 
        font=f, 
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_signup
    )

    tkinter.Label(text="Welcome New Customer! :)", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_address.grid(row=3, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_btn.grid(row=7, column=1, pady=10, padx=20)
    right_frame.pack()
    gender_frame.grid(row=4, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=tkinter.LEFT)
    female_rb.pack(expand=True, side=tkinter.LEFT)
    others_rb.pack(expand=True, side=tkinter.LEFT)
    tkinter.Button(text="Back to Home", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return 

def CustomerLoginPage(root, cursor):
    def validate_login():
        check_counter=0
        warn = ""
        if email_tf.get() == "":
            warn += "\n"
            warn += "Please enter an email!"
        else:
            check_counter += 1
        if pwd_tf.get() == "":
            warn += "\n"
            warn += "Please enter a password!"
        else:
            check_counter += 1
        
        selection_statement = "SELECT customerID, customerName, email, customerPassword FROM Customer WHERE email = %s AND customerPassword = %s"
        
        if check_counter == 2:
            try:
                cursor.execute(selection_statement,(email_tf.get(), pwd_tf.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showinfo('Error', 'Invalid Email and/or Password')
                else:
                    customerID = row[0]
                    customerName = row[1]
                    proceed = messagebox.askyesno(title="Logged in successfully. ", message="Welcome, " + customerName + " !" + "\nProceed to search and buy?")
                    cursor.reset()
                    if proceed:
                        changepage("customerHome")
            except Exception as e:
                messagebox.showerror('Error', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Customer Login')
    ws.config(bg='#0B5A81')

    f = ('Times', 14)

    left_frame = tkinter.Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',   
        relief=tkinter.SOLID, 
        padx=10, 
        pady=10
        )

    tkinter.Label(
        left_frame, 
        text="Enter your Email", 
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        left_frame, 
        text="Enter your Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, pady=10)

    email_tf = tkinter.Entry(
        left_frame, 
        font=f
        )
    pwd_tf = tkinter.Entry(
        left_frame, 
        font=f,
        show='*'
        )
    login_btn = tkinter.Button(
        left_frame, 
        width=15, 
        text='Login', 
        font=f, 
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_login
        )

    tkinter.Label(text="Welcome existing customer! :)", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.pack()
    tkinter.Button(text="Back to Home", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return 

def AdminLoginPage(root, cursor):
    def validate_login_a():
        check_counter=0
        warn = ""
        if phone_tf.get() == "":
            warn += "\n"
            warn += "Please enter a phone number!"
        else:
            check_counter += 1
        if pwd_tf.get() == "":
            warn += "\n"
            warn += "Please enter a password!"
        else:
            check_counter += 1
        
        selection_statement = "SELECT adminID, adminName, phoneNumber, adminPassword FROM Administrator WHERE phoneNumber = %s AND adminPassword = %s"
        
        if check_counter == 2:
            try:
                cursor.execute(selection_statement,(phone_tf.get(), pwd_tf.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showinfo('Error', 'Invalid Phone Number and/or Password')
                else:
                    adminID = row[0]
                    adminName = row[1]
                    messagebox.showinfo("Logged in successfully. ", "Welcome, " + adminName + " !")
                    cursor.reset()
            except Exception as e:
                messagebox.showerror('Error', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Administrator Login')
    ws.config(bg='red')

    f = ('Times', 14)

    left_frame = tkinter.Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',   
        relief=tkinter.SOLID, 
        padx=10, 
        pady=10
        )

    tkinter.Label(
        left_frame, 
        text="Enter your Phone Number", 
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        left_frame, 
        text="Enter your Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, pady=10)

    phone_tf = tkinter.Entry(
        left_frame, 
        font=f
        )
    pwd_tf = tkinter.Entry(
        left_frame, 
        font=f,
        show='*'
        )
    login_btn = tkinter.Button(
        left_frame, 
        width=15, 
        text='Login', 
        font=f, 
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_login_a
        )

    tkinter.Label(text="Welcome existing Administrator! :)", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='red').pack()
    phone_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.pack()
    tkinter.Button(text="Back to Home", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return 

def CustomerBuySearch(root, cursor, currCustomerID):
    for widget in root.winfo_children():
        widget.destroy()
    def getAndUpdateItem(itemID):
        update = "UPDATE item SET purchaseStatus = 'Sold' WHERE itemID = '{}'".format(itemID)
        cursor.execute(update)
        mydb.commit()
    
    def buy_item(itemID):
        if len(itemID) != 4 or not list(items.find({"ItemID":itemID})):
            messagebox.showerror(title="Error", message="Please enter a valid Item ID")
        buy = messagebox.askyesno(message="You are buying item {}".format(itemID))
        if buy:
            if itemSold(cursor, itemID):
                messagebox.showerror(title="Out of stock", message="Item ID {} is out of stock.".format(itemID))
            else:
                getAndUpdateItem(itemID)
                messagebox.showinfo(title="Item purchased!", message="Thank you for your purchase!\nItem bought: " + itemID)
        

    ws = root
    ws.title('Customer - Home')
    ws.config(bg='#0B5A81')
    Label(ws, text="Welcome " + customerName + " [ID:" + customerID + "]",width="300", height="2", font=("Calibri", 13)).pack() 
    Label(ws, text="", bg='#0B5A81').pack() 
    Button(ws, text="Simple search", height="2", width="30", relief=tkinter.SOLID,command= lambda: changepage("simpleSearchPage")).pack()
    Label(ws, text="", bg='#0B5A81').pack() 
    Button(ws, text="Advanced search", height="2", width="30", relief=tkinter.SOLID,command= lambda: changepage("filterSearchPage")).pack()
    Label(ws, text="", bg='#0B5A81').pack() 
    Label(ws, text="To buy, please enter Item ID", width="300", height="2", font=("Calibri", 13)).pack()
    ##for buy entry
    f = ('Times', 14)
    Label(ws, text="Enter item ID here", bg='#CCCCCC', font=f)
    itemid = Entry(ws, font=f)
    itemid.pack()
    Button(ws, text="Buy", height="2", width="30", relief=tkinter.SOLID, command= lambda: buy_item(itemid.get())).pack()
    Label(ws, text="", bg='#0B5A81').pack() 

    return

def simpleSearchPage(root, cursor):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.title('Choose a category!')
    ws.config(bg='#0B5A81')
    tkinter.Label(text="Select category", bg='#0B5A81').pack() 
    # Category
    categories = ["Lights", "Locks"]
    category = StringVar()
    category.set(categories[0])
    dropcat = OptionMenu(root, category, *categories)
    dropcat.pack()

    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Label(text="Select Light model:", bg='#0B5A81').pack()
    # Model
    lights = ["Light1", "Light2", "SmartHome1"]
    light = StringVar()
    light.set(lights[0])
    droplight = OptionMenu(root, light, *lights)
    droplight.pack()

    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Label(text="Select Lock model:", bg='#0B5A81').pack()
    locks = ["Safe1", "Safe2", "Safe3", "SmartHome1"]
    lock = StringVar()
    lock.set(locks[0])
    droplock = OptionMenu(root, lock, *locks)
    droplock.pack()

    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Button(text="Search", height="2", width="30", relief=tkinter.SOLID,command= lambda: SimpleSearchResult(root, cursor, category.get(), (light.get() if category.get() == "Lights" else lock.get()))).pack()
    tkinter.Label(text="", bg='#0B5A81').pack() 
    tkinter.Button(text="Back to Buy/Search page", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: CustomerBuySearch(root,cursor, customerID)).pack(side=tkinter.TOP)
    return



def SimpleSearchResult(root, cursor, cat, mod):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.wm_geometry("850x450")
    ws.title('Search results')
    ws.config(bg='#0B5A81')
    f = ('Calibri', 13)
    Label(text="Search results for category: " + cat + ", model: " + mod, bg='#CCCCCC', font=f).grid(row=0, column=0) 

    # display search result below

    style = ttk.Style()
    style.theme_use("default")
    columns = ('ItemID', 'Color', 'Factory', 'PowerSupply', 'PurchaseStatus', 'ProductionYear', 'Price', 'Warranty (months)')
    tree = ttk.Treeview(root, columns=columns, show = 'headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("#{}".format(i+1), text= columns[i])


    for item in items.find({"Category": cat, "Model":mod}):
        if itemSold(cursor, item['ItemID']):
            continue
        values = (
            item['ItemID'], 
            item['Color'],
            item['Factory'],
            item['PowerSupply'],
            item['PurchaseStatus'],
            item['ProductionYear'],
            itemPriceWarranty(item['Category'], item['Model'])[0],
            itemPriceWarranty(item['Category'], item['Model'])[1]
            )
        tree.insert("", "end", values = values)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(ws, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')


    tkinter.Button(text="Back to Search", height="2", width="30", bg="yellow", relief=tkinter.SOLID,cursor='hand2',command= lambda: simpleSearchPage(root,cursor)).grid(row=2, column=0)
    tkinter.Button(text="To BUY, click here to go to buy/search page", height="2", width="50", bg="green", relief=tkinter.SOLID,cursor='hand2',command= lambda: CustomerBuySearch(root,cursor, customerID)).grid(row=3, column=0)

def itemSold(cursor, itemID):
    # Returns true if item is sold (based on MYSQL item relation) and false otherwise
    return mysqlSelect("SELECT * from item WHERE itemID = '{}'".format(itemID), cursor)[0][4] == 'Sold'

def itemPriceWarranty(cat, mod):
    # Returns (price, warranty) of item's category and model from mongodb products collection
    d = list(products.find({'Category':cat, 'Model':mod}))[0]
    price = d['Price ($)']
    warranty = d['Warranty (months)']
    return (price, warranty)

def changepage(other):
    global currpage, root
    for widget in root.winfo_children():
        widget.destroy()
    if other == "registerCustomer":
        CustomerSignUpPage(root, mycursor, mydb)
        currpage = "registerCustomer"
    elif other == "registerAdmin":
        AdminSignUpPage(root, mycursor, mydb)
        currpage = "registerAdmin"
    elif other == "loginCustomer":
        CustomerLoginPage(root, mycursor)
        currpage = "loginCustomer"
    elif other == "loginAdmin":
        AdminLoginPage(root, mycursor)
        currpage = "loginAdmin"
    elif other == "landing":
        LandingPage(root)
        currpage = "landing"
    elif other == "customerHome":
        currpage = "customerHome"
        CustomerBuySearch(root, mycursor, customerID)
    elif other == "simpleSearchPage":
        currpage = "simpleSearchPage"
        simpleSearchPage(root, mycursor)

def executeSQL(SQLFileName, cursor):    
    with open(SQLFileName, 'r') as SQLscript:
        SQLcommands = SQLscript.read().split(';')
        for command in SQLcommands:
            try:
                cursor.execute(command)
            except:
                print('Statement not executed: ' + str(command))

def mysqlSelect(command, cursor):
    # Select
    cursor.execute(command)
    result = cursor.fetchall()
    return result

# Global variables

customerName = ""
customerID = ""

# Connect MYSQL
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Valentin1" #your pw here since everyone got diff pw
MYSQL_DATABASE = "oshes"

mydb = mysql.connector.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DATABASE)
mycursor = mydb.cursor(buffered=True)

# Connect MongoDB
client = MongoClient()
mongo = client['Inventory']
items = mongo.items
products = mongo.products

#init_mysql()

currpage = "landing"
root = tkinter.Tk() 
root.wm_geometry("600x600")
LandingPage(root)
root.mainloop()