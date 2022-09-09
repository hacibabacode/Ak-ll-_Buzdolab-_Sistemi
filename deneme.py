
# importing sqlite3 module
import sqlite3
 
# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('product_data.db')
 
 
# insert query to insert food  details
# in the above table
connection.execute("INSERT INTO product VALUES (1, 'cakes',800,10 )");
connection.execute("INSERT INTO product VALUES (2, 'Salatalik',100,20 )");
connection.execute("INSERT INTO product VALUES (3, 'Kola',1000,30 )");
connection.execute("INSERT INTO product VALUES (4, 'Sut',1000,30 )");
connection.execute("INSERT INTO product VALUES (5, 'Peynir',1000,30 )");
 
 
print("Food id and Food Name\n")
 
# create a cousor object for select query
cursor = connection.execute("SELECT FIND,FNAME from product ")
 
# display all data from FOOD1 table
for row in cursor:
     print(row)