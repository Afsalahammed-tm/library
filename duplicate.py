# CREATE DATABASE library_db;

# USE library_db;

# CREATE TABLE members (
#     member_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     contact VARCHAR(15) NOT NULL
# );

# CREATE TABLE books (
#     book_id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(100) NOT NULL,
#     author VARCHAR(100) NOT NULL,
#     available BOOLEAN DEFAULT TRUE
# );

# CREATE TABLE borrowed_books (
#     borrow_id INT AUTO_INCREMENT PRIMARY KEY,
#     member_id INT,
#     book_id INT,
#     borrow_date DATE,
#     due_date DATE,
#     FOREIGN KEY (member_id) REFERENCES members(member_id),
#     FOREIGN KEY (book_id) REFERENCES books(book_id)
# );

import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime, timedelta

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # Add your MySQL password here
        database="library_db"
    )

# Main application class
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.add_member_tab = tk.Frame(self.notebook)
        self.add_book_tab = tk.Frame(self.notebook)
        self.borrow_book_tab = tk.Frame(self.notebook)
        self.view_records_tab = tk.Frame(self.notebook)

        self.notebook.add(self.add_member_tab, text="Add Member")
        self.notebook.add(self.add_book_tab, text="Add Book")
        self.notebook.add(self.borrow_book_tab, text="Borrow Book")
        self.notebook.add(self.view_records_tab, text="View Records")

        # Add Member Tab
        self.setup_add_member_tab()
        # Add Book Tab
        self.setup_add_book_tab()
        # Borrow Book Tab
        self.setup_borrow_book_tab()
        # View Records Tab
        self.setup_view_records_tab()

    # Add Member Tab
    def setup_add_member_tab(self):
        tk.Label(self.add_member_tab, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.member_name = tk.Entry(self.add_member_tab)
        self.member_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.add_member_tab, text="Contact:").grid(row=1, column=0, padx=10, pady=10)
        self.member_contact = tk.Entry(self.add_member_tab)
        self.member_contact.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.add_member_tab, text="Add Member", command=self.add_member).grid(row=2, column=0, columnspan=2, pady=10)

    # Add Book Tab
    def setup_add_book_tab(self):
        tk.Label(self.add_book_tab, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        self.book_title = tk.Entry(self.add_book_tab)
        self.book_title.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.add_book_tab, text="Author:").grid(row=1, column=0, padx=10, pady=10)
        self.book_author = tk.Entry(self.add_book_tab)
        self.book_author.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.add_book_tab, text="Add Book", command=self.add_book).grid(row=2, column=0, columnspan=2, pady=10)

    # Borrow Book Tab
    def setup_borrow_book_tab(self):
        tk.Label(self.borrow_book_tab, text="Member ID:").grid(row=0, column=0, padx=10, pady=10)
        self.borrow_member_id = tk.Entry(self.borrow_book_tab)
        self.borrow_member_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.borrow_book_tab, text="Book ID:").grid(row=1, column=0, padx=10, pady=10)
        self.borrow_book_id = tk.Entry(self.borrow_book_tab)
        self.borrow_book_id.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.borrow_book_tab, text="Borrow Book", command=self.borrow_book).grid(row=2, column=0, columnspan=2, pady=10)

    # View Records Tab
    def setup_view_records_tab(self):
        self.tree = ttk.Treeview(self.view_records_tab, columns=("ID", "Name", "Contact", "Book Title", "Borrow Date", "Due Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Book Title", text="Book Title")
        self.tree.heading("Borrow Date", text="Borrow Date")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.pack(fill="both", expand=True)

        tk.Button(self.view_records_tab, text="Refresh", command=self.load_records).pack(pady=10)

    # Add Member Function
    def add_member(self):
        name = self.member_name.get()
        contact = self.member_contact.get()

        if name and contact:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members (name, contact) VALUES (%s, %s)", (name, contact))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Member added successfully!")
            self.member_name.delete(0, tk.END)
            self.member_contact.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    # Add Book Function
    def add_book(self):
        title = self.book_title.get()
        author = self.book_author.get()

        if title and author:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book added successfully!")
            self.book_title.delete(0, tk.END)
            self.book_author.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    # Borrow Book Function
    def borrow_book(self):
        member_id = self.borrow_member_id.get()
        book_id = self.borrow_book_id.get()

        if member_id and book_id:
            conn = connect_db()
            cursor = conn.cursor()

            # Check if the book is available
            cursor.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
            book_status = cursor.fetchone()

            if book_status and book_status[0]:
                borrow_date = datetime.now().strftime("%Y-%m-%d")
                due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

                cursor.execute("INSERT INTO borrowed_books (member_id, book_id, borrow_date, due_date) VALUES (%s, %s, %s, %s)",
                               (member_id, book_id, borrow_date, due_date))
                cursor.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Book borrowed successfully!")
                self.borrow_member_id.delete(0, tk.END)
                self.borrow_book_id.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Book is not available.")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    # Load Records Function
    def load_records(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.member_id, m.name, m.contact, b.title, bb.borrow_date, bb.due_date
            FROM borrowed_books bb
            JOIN members m ON bb.member_id = m.member_id
            JOIN books b ON bb.book_id = b.book_id
        """)
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", "end", values=row)
            
            
CREATE DATABASE library_db;

USE library_db;

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15) NOT NULL
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE borrowed_books (
    borrow_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    due_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()