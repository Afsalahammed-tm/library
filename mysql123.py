import mysql.connector
print("mmmmm")
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    auth_plugin='mysql_native_password',
    database="alaska"
)
print("successfully connected")
cursor1=conn.cursor()
# cursor1.execute("create database alaska")
# print("awsd")

cursor1.execute("create table student(id int primary key,name varchar(30),phoneno bigint,course varchar(30))")
print("successfully created table")

# cursor1.execute('insert into student(id,name,phoneno,course) values(1,"anu",80452367,"python")')
# conn.commit()
# print("done")

# x='insert into student(id,name,phoneno,course) values(%s,%s,%s,%s)'
# y=[(2,'ammu',71215757,'java'),(3,"jack",954214674,'php')]
# cursor1.executemany(x,y)
# conn.commit()
# print(" insert multiple value")

# cursor1.execute('select * from student')
# print("show table")
# x=cursor1.fetchall()
# # print(x)
# for i in x:
#     print(i)

# cursor1.execute('select * from student')
# x=cursor1.fetchone()
# print(x)

# cursor1.execute("delete from student where id=2")
# conn.commit()
# print("deleted")

