import sqlite3

con=sqlite3.connect('jujutsu_high_data.db')
    
c=con.cursor()
    
c.execute('DROP TABLE feedback')

a=c.fetchall()
print(a)