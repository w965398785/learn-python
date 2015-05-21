#-*- coding:utf-8 -*-
import sqlite3


conn = sqlite3.connet('student.db')
print"Opended database successfully";
conn.execute('''CREATE TABLE people
       (ID  INT PRIMARY KEY     NOT NULL,
	  name              TEXT    NOT NULL,
	  AGE               TNT     NOT NULL,
	  SEX               TEXT    NOT NULL
	  score             TNT );''')
print"table created successfully';
conn.close()
conn = sqlite3.connect('student.db')
print"Opended database successfully";

conn.execute("INSERT INTO people (ID,name,AGE,sex,score) \
     VALUES (1, 'Áø¿­Ô´',19,'ÄÐ',23)");

conn.execute("INSERT INTO people (ID,name,AGE,sex,score) \
      VALUES (2,'Áø¿­Ô´',19,'Å®',23)");
conn.commit.()
print "records created successfully";
conn.slose()

conn = sqlite3.connect('student.db')
	 
import sqlite3

conn = sqlite3.connect('student.db')
print "Opened database successfully";

conn.execute("DELETE from people where ID=2;")
conn.commit
print "Total number of rows deleted :", conn.total_changes

cursor = conn.execute("SELECT id, name, asex, score from people")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "sex = ", row[2]
   print "score = ", row[3],
   print "AGE = " row[4] "\n"

print "Operation done successfully";
conn.close()
import sqlite3

conn = sqlite3.connect('student.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, sex, score from people")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "sex = ", row[2]
   print "score = ", row[3],
   print "AGE = " row[4]   "\n"

print "Operation done successfully";
conn.close()
import sqlite3

conn = sqlite3.connect('student.db')
print "Opened database successfully";

conn.execute("UPDATE people set score = 26 where ID=1")
conn.commit
print "Total number of rows updated :", conn.total_changes

cursor = conn.execute("SELECT id, name, sex, score from people")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "sex = ", row[2]
   print "score = ", row[3],
   print "AGE = ", row[4]   "\n"

print "Operation done successfully";
conn.close()


conn = sqlite3.connect('student.db')
print "Opended database successfully";
cursor = conn.execute("SELECT ID,name,AGE,sex,score from people")
for row in cursor:
    print "NAME = ", row[1],"AGE = ",rows[2],"sex = ",row[3], "score = ",row[4]
	
print "Operation done successfully";
conn.close

