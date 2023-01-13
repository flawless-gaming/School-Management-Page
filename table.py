#create table

#modules
import sqlite3

#function to create table
def create():
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    #command to create table
    c.execute('CREATE TABLE if not exists admission(st_id integer,st_name text,st_age integer,st_gender text,st_exp text,st_type text,st_encounter integer,st_teacher text)')
    
    c.execute('CREATE TABLE if not exists teacher(t_id integer,t_name text,t_age integer,t_gender text,t_exp integer,t_encounter integer)')
    
    c.execute('CREATE TABLE if not exists feedback(f_name text,f_email text,f_rating text,f_opinion text)')
    #to close connection from database
    con.commit()
        
    con.close()
    
    
