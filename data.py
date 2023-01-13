#modules
import sqlite3
#output of all teachers data
print('xxxxxxxx teachers xxxxxxxxx')
#connecting to data base
con=sqlite3.connect('jujutsu_high_data.db')
        
c=con.cursor()
#command to get all data
c.execute('SELECT * FROM teacher')
#to fetchall data
t_data=c.fetchall()
#to show all data fetched
for i in t_data:
    print(i)
#output of all students data
print('xxxxxx students xxxxxxx')
#command to get all data
c.execute('SELECT * FROM admission')
#to fetch all data
st_data=c.fetchall()
#to show all data fetched
for j in st_data:
    print(j)
#output of all feedback data taken
print('xxxxxxxx feedback xxxxxxxxx')
#command to get all data
c.execute('SELECT * FROM feedback')
# to fetch all data
f_data=c.fetchall()
#to show all data fetched
for k in f_data:
    print(k)
