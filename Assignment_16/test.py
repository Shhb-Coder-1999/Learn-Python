import sqlite3

conn = sqlite3.connect("Contacts.db")
my_cursor = conn.cursor()

my_cursor.execute("SELECT * FROM Persons")

Result = my_cursor.fetchall()

print(Result)