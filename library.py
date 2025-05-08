from tkinter import *
from tkinter import ttk
# from tkinter.ttk import Combobox
import tkinter
from tkinter import messagebox
import datetime

import sqlite3
import tkinter.messagebox

conn=sqlite3.connect("new.db")
my_cursor=conn.cursor()
# my_cursor.execute("create table Librarydata (member_type varchar(30),prno varchar(30),idno varchar(30) primary key,firstname VARCHAR(45),lastname VARCHAR(45),address VARCHAR(45),pincode VARCHAR(45),mobile VARCHAR(45),bookid VARCHAR(45),booktitle VARCHAR(45),author VARCHAR(45),dateborrowed VARCHAR(45),datedue VARCHAR(45),days VARCHAR(45),dateoverdue VARCHAR(45), fine VARCHAR(45))")



class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x900")
        
        
        # ***************************** variable ************************
        
        
        # These lines are creating Tkinter variables like StringVar() and IntVar(). They are special types of variables provided by Tkinter to dynamically store and update values in GUI applications.
        #These variables are linked to entry fields or other widgets in the GUI
        #When the user enters data into an input field, the value is automatically stored in these variables, and you can retrieve or update the data easily.
        
        
        
        
        
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.pincode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.days_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.fine_var=StringVar()
        
        # The reason StringVar() in Tkinter and VARCHAR in MySQL are often used, even for things like ID numbers, PRN, mobile numbers, pincode, dates, etc., which seem numeric, is mostly due to the nature of the data and how it's handled in different contexts.
        # Tkinter’s input fields (Entry widgets) generally handle data as strings. Whatever the user types in an Entry field, it’s treated as a string.
        
        #   That’s why StringVar() is often used to capture user input, even if the data looks like a number.
        # Mobile Number: 9876543210 → It's a number, but you don’t need to perform calculations with it. You just display/store it, so treating it as a string is easier.
        
        
        
        # *********************** title *************************************
        label_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        label_title.pack(side=TOP,fill=X)
        
         # *********************** full middle frame *************************************
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="aqua")
        frame.place(x=0,y=130,width=1357,height=370)
        
        
        
         # *********************** left middle frame *************************************
        Data_left=LabelFrame(frame,text="Library Membership Information",bg="aqua",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        Data_left.place(x=0,y=5,width=750,height=325)
        
        label_member=Label(Data_left,bg="aqua",text="Member Type: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_member.grid(row=0,column=0,sticky=W)
        
        cc=ttk.Combobox(Data_left,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        cc["value"]=("Admin Staff","Student","Lecturer")
        cc.grid(row=0,column=1)
        
        label_pr=Label(Data_left,font=("times new roman",12,"bold"),text="PR No: ",padx=2,pady=6,bg="aqua")
        label_pr.grid(row=1,column=0,sticky=W)
        e1=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=29)
        e1.grid(row=1,column=1)
        
        label_id=Label(Data_left,font=("times new roman",12,"bold"),text="ID No: ",padx=2,pady=6,bg="aqua")
        label_id.grid(row=2,column=0,sticky=W)
        e2=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.id_var,width=29)
        e2.grid(row=2,column=1)
        
        label_fname=Label(Data_left,font=("times new roman",12,"bold"),text="First Name: ",padx=2,pady=6,bg="aqua")
        label_fname.grid(row=3,column=0,sticky=W)
        e3=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.firstname_var,width=29)
        e3.grid(row=3,column=1)
        
        label_lname=Label(Data_left,font=("times new roman",12,"bold"),text="Last Name: ",padx=2,pady=6,bg="aqua")
        label_lname.grid(row=4,column=0,sticky=W)
        e4=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.lastname_var,width=29)
        e4.grid(row=4,column=1)
        
        label_addr1=Label(Data_left,font=("times new roman",12,"bold"),text="Address: ",padx=2,pady=6,bg="aqua")
        label_addr1.grid(row=5,column=0,sticky=W)
        e5=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.address_var,width=29)
        e5.grid(row=5,column=1)
        
        label_pincode=Label(Data_left,font=("times new roman",12,"bold"),text="Pincode: ",padx=2,pady=6,bg="aqua")
        label_pincode.grid(row=6,column=0,sticky=W)
        e7=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.pincode_var,width=29)
        e7.grid(row=6,column=1)
        
        label_mobile=Label(Data_left,font=("times new roman",12,"bold"),text="Mobile: ",padx=2,pady=6,bg="aqua")
        label_mobile.grid(row=7,column=0,sticky=W)
        e8=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.mobile_var,width=29)
        e8.grid(row=7,column=1)
        
        label_bookid=Label(Data_left,font=("times new roman",12,"bold"),text="Book ID: ",padx=2,pady=6,bg="aqua")
        label_bookid.grid(row=0,column=2,sticky=W)
        e9=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=29)
        e9.grid(row=0,column=3)
        
        label_btitle=Label(Data_left,font=("times new roman",12,"bold"),text="Book Title: ",padx=2,pady=6,bg="aqua")
        label_btitle.grid(row=1,column=2,sticky=W)
        e10=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=29)
        e10.grid(row=1,column=3)
        
        label_name=Label(Data_left,font=("times new roman",12,"bold"),text="Author Name: ",padx=2,pady=6,bg="aqua")
        label_name.grid(row=2,column=2,sticky=W)
        e11=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.author_var,width=29)
        e11.grid(row=2,column=3)
        
        label_dateborrowed=Label(Data_left,font=("times new roman",12,"bold"),text="Date Borrowed: ",padx=2,pady=6,bg="aqua")
        label_dateborrowed.grid(row=3,column=2,sticky=W)
        e12=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        e12.grid(row=3,column=3)
        
        label_datedue=Label(Data_left,font=("times new roman",12,"bold"),text="Date Due: ",padx=2,pady=6,bg="aqua")
        label_datedue.grid(row=4,column=2,sticky=W)
        e13=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=29)
        e13.grid(row=4,column=3)
        
        label_days=Label(Data_left,font=("times new roman",12,"bold"),text="Days on Book: ",padx=2,pady=6,bg="aqua")
        label_days.grid(row=5,column=2,sticky=W)
        e14=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.days_var,width=29)
        e14.grid(row=5,column=3)
        
        
        label_dateoverdue=Label(Data_left,font=("times new roman",12,"bold"),text="Date Over Due: ",padx=2,pady=6,bg="aqua")
        label_dateoverdue.grid(row=6,column=2,sticky=W)
        cc1=ttk.Combobox(Data_left,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=27,state="readonly")
        cc1["value"]=("No","Yes")
        cc1.grid(row=6,column=3)
        # e15=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        # e15.grid(row=6,column=3)
        
        
        label_late=Label(Data_left,font=("times new roman",12,"bold"),text="Late Return Fine: ",padx=2,pady=6,bg="aqua")
        label_late.grid(row=7,column=2,sticky=W)
        e16=Entry(Data_left,font=("times new roman",12,"bold"),textvariable=self.fine_var,width=29)
        e16.grid(row=7,column=3)
        
        
        
        
         # *********************** right middle frame *************************************
        Data_right=LabelFrame(frame,text="Book Details",bg="aqua",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        Data_right.place(x=758,y=5,width=540,height=325)
        
        self.txtBox=Text(Data_right,font=("times new roman",12,"bold"),width=37,height=14,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(Data_right)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        list_books = [
    # Classic Fiction
            "Pride and Prejudice",
            "To Kill a Mockingbird",
            "1984 - George Orwell",
            "The Great Gatsby",
            "Moby-Dick",

            # Fantasy
            "The Hobbit",
            "Harry Potter and the Sorcerer’s Stone ",
            "The Name of the Wind ",
            "Mistborn: The Final Empire ",
            "The Lies of Locke Lamora ",

            # Science Fiction
            "Dune ",
            "The Hitchhiker’s Guide to the Galaxy ",
            "Neuromancer ",
            "Snow Crash ",
            "The Left Hand of Darkness ",

            # Mystery & Thriller
            "Gone Girl ",
            "The Girl with the Dragon Tattoo ",
            "Sherlock Holmes: A Study in Scarlet ",
            "The Da Vinci Code ",
            "Big Little Lies",

            # Horror
            "Dracula ",
            "It ",
            "The Haunting of Hill House ",
            "Bird Box  ",
            "The Exorcist ",

            # Historical Fiction
            "The Book Thief ",
            "All the Light We Cannot See",
            "The Nightingale",
            "The Pillars of the Earth",
            "Memoirs of a Geisha ",

            # Young Adult (YA)
            "The Hunger Games",
            "Percy Jackson & The Lightning Thief ",
            "Divergent ",
            "A Court of Thorns and Roses ",
            "Six of Crows ",

            # Literary Fiction
            "The Road ",
            "Where the Crawdads Sing ",
            "The Alchemist ",
            "The Shadow of the Wind",
            
        ]
        
       

        
        def Selectbook(event=""):
            try:
                value = str(listBox.get(listBox.curselection())).strip()
                
        

        
                book_details = {
                    "Pride and Prejudice": "Jane Austen",
                    "To Kill a Mockingbird": "Harper Lee",
                    "1984 - George Orwell": "George Orwell",
                    "The Great Gatsby": "F. Scott Fitzgerald",
                    "Moby-Dick": "Herman Melville",
                    "The Hobbit": "J.R.R. Tolkien",
                    "Harry Potter and the Sorcerer’s Stone": "J.K. Rowling",
                    "The Name of the Wind": "Patrick Rothfuss",
                    "Mistborn: The Final Empire": "Brandon Sanderson",
                    "The Lies of Locke Lamora": "Scott Lynch",
                    "Dune": "Frank Herbert",
                    "The Hitchhiker’s Guide to the Galaxy": "Douglas Adams",
                    "Neuromancer": "William Gibson",
                    "Snow Crash": "Neal Stephenson",
                    "The Left Hand of Darkness": "Ursula K. Le Guin",
                    "Gone Girl": "Gillian Flynn",
                    "The Girl with the Dragon Tattoo": "Stieg Larsson",
                    "Sherlock Holmes: A Study in Scarlet": "Arthur Conan Doyle",
                    "The Da Vinci Code": "Dan Brown",
                    "Big Little Lies": "Liane Moriarty",
                    "Dracula": "Bram Stoker",
                    "It": "Stephen King",
                    "The Haunting of Hill House": "Shirley Jackson",
                    "Bird Box": "Josh Malerman",
                    "The Exorcist": "William Peter Blatty",
                    "The Book Thief": "Markus Zusak",
                    "All the Light We Cannot See": "Anthony Doerr",
                    "The Nightingale": "Kristin Hannah",
                    "The Pillars of the Earth": "Ken Follett",
                    "Memoirs of a Geisha": "Arthur Golden",
                    "The Hunger Games": "Suzanne Collins",
                    "Percy Jackson & The Lightning Thief": "Rick Riordan",
                    "Divergent": "Veronica Roth",
                    "A Court of Thorns and Roses": "Sarah J. Maas",
                    "Six of Crows": "Leigh Bardugo",
                    "The Road": "Cormac McCarthy",
                    "Where the Crawdads Sing": "Delia Owens",
                    "The Alchemist": "Paulo Coelho",
                    "The Shadow of the Wind": "Carlos Ruiz Zafón",
                }

                if value in book_details:
                    book_id = f"BKID{1000 + list(book_details.keys()).index(value) + 1}"
                    self.bookid_var.set(book_id)
                    self.booktitle_var.set(value)
                    self.author_var.set(book_details[value])

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2

                    self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
                    self.datedue_var.set(d3.strftime("%Y-%m-%d"))
                    self.days_var.set(15)
                    self.fine_var.set("Rs ")
                    
                
            except:
                pass
            
        
               
            
        
        
        
    



        listBox=Listbox(Data_right,font=("times new roman",12,"bold"),width=22,height=14)
            # for item in list_books:
            #     listBox.insert(END,item)
            
        listBox.bind("<<ListboxSelect>>",Selectbook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)  # used to link a scrollbar (listScrollbar) to a listbox (listBox), allowing the scrollbar to scroll the listbox content vertically.
        
        for item in list_books:
            listBox.insert(END,item)

        
    # ******************** add,update,delete buttons **********************************
        
        frame_button=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="aqua")
        frame_button.place(x=0,y=506,width=1357,height=50)
        
        btnAdddata=Button(frame_button,command=self.adda_data,text="ADD",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=0)
        
        btnAdddata=Button(frame_button,command=self.showdata, text="SHOW",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=1)
        
        btnAdddata=Button(frame_button,command=self.update,text="UPDATE",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=2)
        
        btnAdddata=Button(frame_button,command=self.delete,text="DELETE",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=3)
        
        btnAdddata=Button(frame_button,command=self.reset,text="RESET",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=4)
        
        btnAdddata=Button(frame_button,command=self.exit,text="EXIT",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAdddata.grid(row=0,column=5)
        
        # ******************** Information Frame **********************************
        
        frame_info=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="aqua")
        frame_info.place(x=0,y=562,width=1357,height=128)
        
        table_frame=Frame(frame_info,bd=6,relief=RIDGE,bg="aqua")
        table_frame.place(x=0,y=2,width=1300,height=108)
        
        xscroll=Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=Scrollbar(table_frame,orient=VERTICAL)
        #-------------- The ttk.Treeview() widget in Tkinter is used to create a table-like structure or hierarchical view. It is often used to display data in rows and columns, similar to a spreadsheet.----------
        self.library_table=ttk.Treeview(table_frame,column=("membertype","prno","idno","fname","lname","address","pincode","mobile","bookid","title","author","dateborrowed","datedue","days","dateoverdue","fine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)  # horizontal and vertical scrollbar
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prno",text="PR No")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("fname",text="First Name")
        self.library_table.heading("lname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("pincode",text="Pincode")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("title",text="Book Title")
        self.library_table.heading("author",text="Author Name")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("fine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("fname",width=100)
        self.library_table.column("lname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("pincode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("fine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.fetchdata()
        self.library_table.bind("<ButtonRelease-1>",self.cursor)



    # to add data to the database
    def adda_data(self):
        # This line creates a cursor object. A cursor is used to execute SQL queries in the database.
        # my_cursor=conn.cursor()

        # my_cursor.execute("create database done")
        # my_cursor.execute("create table library (member_type varchar(30),prno varchar(30),idno varchar(30) primary key,firstname VARCHAR(45),lastname VARCHAR(45),address VARCHAR(45),pincode VARCHAR(45),mobile VARCHAR(45),bookid VARCHAR(45),booktitle VARCHAR(45),author VARCHAR(45),dateborrowed VARCHAR(45),datedue VARCHAR(45),days VARCHAR(45),dateoverdue VARCHAR(45), fine VARCHAR(45))")
        
        my_cursor.execute("insert into Librarydata values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.member_var.get(),self.prn_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.pincode_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.days_var.get(),self.dateoverdue_var.get(),self.fine_var.get()))
        conn.commit() #  save the changes made to the database
        self.fetchdata()
        
        messagebox.showinfo("Member has been inserted successfully")
        
    def update(self):
        my_cursor.execute("update Librarydata set member_type=?,prno=?,firstname=?,lastname=?,address=?,pincode=?,mobile=?,bookid=?,booktitle=?,author=?,dateborrowed=?,datedue=?,days=?,dateoverdue=?,fine=? where idno=? ",(self.member_var.get(),self.prn_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.pincode_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.days_var.get(),self.dateoverdue_var.get(),self.fine_var.get(),self.id_var.get()))
        conn.commit() 
        self.fetchdata()
        self.reset()
        messagebox.showinfo("Member has been updated successfully")
        
    def fetchdata(self): # self refers to the instance of the class.
        my_cursor.execute("select * from Librarydata")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children()) # self.library_table.delete(*self.library_table.get_children()) → Deletes all existing rows from the table before inserting new ones.
            # The * (asterisk) is used to unpack the list of row IDs, passing them as separate arguments.
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        
        
    def cursor(self,event=""):
        cursor_row=self.library_table.focus() #   Gets the currently selected row's ID in the Treeview table Stores this row ID in cursor_row.
        content=self.library_table.item(cursor_row)
        row=content["values"] #  extracts the actual data values from the selected row.
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address_var.set(row[5])
        self.pincode_var.set(row[6])
        self.mobile_var.set(row[7])
        self.bookid_var.set(row[8])
        self.booktitle_var.set(row[9])
        self.author_var.set(row[10])
        self.dateborrowed_var.set(row[11])
        self.datedue_var.set(row[12])
        self.days_var.set(row[13])
        self.dateoverdue_var.set(row[14])
        self.fine_var.set(row[15])
        
    def showdata(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() +"\n")
        self.txtBox.insert(END,"PR No:\t\t"+ self.id_var.get() +"\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.prn_var.get() +"\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() +"\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() +"\n")
        self.txtBox.insert(END,"Address:\t\t"+ self.address_var.get() +"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+ self.pincode_var.get() +"\n")
        self.txtBox.insert(END,"Mobile:\t\t"+ self.mobile_var.get() +"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() +"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() +"\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() +"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+ self.dateborrowed_var.get() +"\n")
        self.txtBox.insert(END,"Date Due:\t\t"+ self.datedue_var.get() +"\n")
        self.txtBox.insert(END,"Days:\t\t"+ self.days_var.get() +"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() +"\n")
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.fine_var.get() +"\n")
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.pincode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.days_var.set(""),
        self.dateoverdue_var.set(""),
        self.fine_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def exit(self):
        exit=tkinter.messagebox.askyesno("Library Management System","Are you sure you want to EXIT") 
        if exit>0:
            self.root.destroy()
            return   

    def delete(self):
        if self.id_var.get()=="":
            messagebox.showerror("Select any")
        else:
            query="delete from Librarydata where idno=?"
            g=(self.id_var.get(),)
            my_cursor.execute(query,g)
            # my_cursor.execute("delete from Librarydata where idno=?",(self.id_var.get(),))
            conn.commit()
            self.fetchdata()
            self.reset()
            messagebox.showinfo("Deleted Successfully")
if __name__ == "__main__":
    root=Tk()
    
    obj=Library(root)     # root is the name of the window
    root.mainloop()