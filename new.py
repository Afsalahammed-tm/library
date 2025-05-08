# import mysql.connector

# conn=mysql.connector.connect(host="localhost",user="root",password="root", port=3306,database="new")
# print("helo")
# my_cursor=conn.cursor()
# print("hello")


import sqlite3

conn=sqlite3.connect("new.db")
print("helo")
my_cursor=conn.cursor()
print("hello")