import sqlite3 
    
connection = sqlite3.connect("myTable.db") 
    
crsr = connection.cursor() 
   
sql_command = """CREATE TABLE emp (  
staff_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""
crsr.execute(sql_command) 
  
sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 
   
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 

sql_command = """SELECT * FROM emp"""  
crsr.execute(sql_command)
  
ans= crsr.fetchall()  
  
for i in ans: 
    print(i) 
 
connection.commit() 
   
connection.close() 

  