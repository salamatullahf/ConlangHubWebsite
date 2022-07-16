import sqlite3

conn = sqlite3.connect('database.db')
print
'Opened database successfully'

conn.execute('DROP TABLE applicants')
print
'Table DROPPED successfully'

conn.execute('CREATE TABLE contacts (name TEXT, email TEXT, msg TEXT, type TEXT)')
print
'Table created successfully'


conn.close()
