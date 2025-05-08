import datetime
import tkinter as tk
from tkinter import StringVar, IntVar, ttk

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")

        # Dictionary to store book details
        self.books = {
            "Pride and Prejudice": {
                "book_id": "BKID4534",
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "fine": "Rs.30",
                "days": 15
            },
            "Halloween": {
                "book_id": "BKID5678",
                "title": "Halloween",
                "author": "John Carpenter",
                "fine": "Rs.40",
                "days": 10
            },
            "To Kill a Mockingbird": {
                "book_id": "BKID6789",
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "fine": "Rs.35",
                "days": 12
            }
        }

        # Variables to store book details
        self.selected_book = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.days_var = IntVar()
        self.dateoverdue_var = StringVar()
        self.fine_var = StringVar()

        # GUI Elements
        tk.Label(root, text="Select a Book:", font=("Arial", 12)).pack(pady=5)
        self.book_dropdown = ttk.Combobox(root, textvariable=self.selected_book, values=list(self.books.keys()), state="readonly")
        self.book_dropdown.pack(pady=5)
        self.book_dropdown.bind("<<ComboboxSelected>>", self.Selectbook)

        # Labels and Entry Fields
        self.create_label_entry("Book ID:", self.bookid_var)
        self.create_label_entry("Title:", self.booktitle_var)
        self.create_label_entry("Author:", self.author_var)
        self.create_label_entry("Date Borrowed:", self.dateborrowed_var)
        self.create_label_entry("Due Date:", self.datedue_var)
        self.create_label_entry("Days Allowed:", self.days_var)
        self.create_label_entry("Overdue Status:", self.dateoverdue_var)
        self.create_label_entry("Fine:", self.fine_var)

    def create_label_entry(self, label_text, var):
        frame = tk.Frame(self.root)
        frame.pack(pady=2, fill="x", padx=10)
        tk.Label(frame, text=label_text, width=15, anchor="w").pack(side="left")
        tk.Entry(frame, textvariable=var, state="readonly").pack(side="left", fill="x", expand=True)

    def Selectbook(self, event):
        book_name = self.selected_book.get()
        if book_name in self.books:
            book = self.books[book_name]

            # Setting book details
            self.bookid_var.set(book["book_id"])
            self.booktitle_var.set(book["title"])
            self.author_var.set(book["author"])

            # Calculating dates
            d1 = datetime.datetime.today()
            d3 = d1 + datetime.timedelta(days=book["days"])

            self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
            self.datedue_var.set(d3.strftime("%Y-%m-%d"))
            self.days_var.set(book["days"])
            self.dateoverdue_var.set("No")
            self.fine_var.set(book["fine"])

# Running the Application
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()



