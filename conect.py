import mysql.connector

sales_data = mysql.connector.connect(host="localhost", user="root", passwd="lgl90d410", database="project")

if sales_data.is_connected():
    print("Connected")
    sales_data.close()
    print("Connection closed")