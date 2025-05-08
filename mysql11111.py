import sqlite3
mydb=sqlite3.connect('hellllo.db')
# print("hi")
cursor1=mydb.cursor()
# cursor1.execute("create table sept1(id int primary key not null,name text not null,age int not null,salary int not null)")
# cursor1.execute("insert into sept1(id,name,age,salary) values (1,'ammu',20,23000),(2,'anu',29,89000)")
# mydb.commit()
# print("done")
# cursor1.execute("update sept1 set salary=9000 where id=1")
# mydb.commit()


cursor1.execute("select * from sept1")
x=cursor1.fetchall()
# x=cursor1.fetchone()
print(x)