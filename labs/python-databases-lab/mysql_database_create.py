# mysql_database.oy
# Calling the sql commands in python 
# Author: John Crumlish

import mysql.connector 
 
connection = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password="" 
) 
 
mycursor = connection.cursor() 
 
mycursor.execute("CREATE database wsaa") 
mycursor.close() 
connection.close()