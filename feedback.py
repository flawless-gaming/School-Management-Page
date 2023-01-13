#feedback form

#modules
from tkinter import *
from PIL import Image,ImageTk
import sqlite3
import table

#function to send data to database
def send():
    table.create()#to create table
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    #command to add all data in database
    c.execute('INSERT INTO feedback VALUES(:f_name,:f_email,:f_rating,:f_opinion)',
              {'f_name':name_box.get(),
               'f_email':email_box.get()+email_type.get(),
               'f_rating':rating.get(),
               'f_opinion':opinion_box.get('0.0','end')
                  })
    print(name_box.get(),email_box.get()+email_type.get(),rating.get(),opinion_box.get('1.0','end'))
    #to close connection from database
    con.commit()
    con.close()

#function to take in feedback from user
def feedback():
    #window created
    feed=Toplevel()
    #window title
    feed.title('Feedback')
    feed.iconbitmap('download.ico')#window icon
    feed.geometry('555x455')#window size
    
    #background image of window
    bg=ImageTk.PhotoImage(Image.open('feedback.png'))
    label=Label(feed,image=bg)
    label.place(x = 0,y = 0)
    
    global name_box
    global email_box
    global email_type
    global rating
    global opinion_box
    #data
    title=Label(feed,text='Feedback',font=('Showcard Gothic',20),padx=20)
    title.place(x=200,y=20)
    
    name_label=Label(feed, text='Name',font=('Showcard Gothic',10))
    name_label.place(x=160,y=80)
    
    name_box=Entry(feed,font=('Showcard Gothic',10),width=25)
    name_box.place(x=230,y=80)
    
    email_label=Label(feed, text='Email',font=('Showcard Gothic',10))
    email_label.place(x=160,y=110)
    
    email_box=Entry(feed,font=('Showcard Gothic',10),width=25)
    email_box.place(x=230,y=110)
    
    type_=['@gmail.com',
           '@outlook.com',
           '@hotmail.com ',
           '@aol.com',
           '@aim.com',
           '@yahoo.com ',
           '@icloud.com ',
           '@protonmail.com',
           '@zoho.com ',
           '@yandex.com ',
           '@titan.email',
           '@gmx.com',
           '@hubspot.com ',
           '@mail.com ',
           '@tutanota.com']
    email_type=StringVar()
    email_type_box=OptionMenu(feed,email_type,*type_)
    email_type_box.place(x=440,y=110)
    
    rating_label=Label(feed,text='Rating',font=('Showcard Gothic',10),padx=10)
    rating_label.place(x=160,y=140)
    
    rating=StringVar()
    
    excellent=Checkbutton(feed,text='Excellent',font=('Showcard Gothic',10),variable=rating,onvalue='Excellent')
    excellent.deselect()
    excellent.place(x=160,y=170)
    
    good=Checkbutton(feed,text='Good',font=('Showcard Gothic',10),variable=rating,onvalue='Good')
    good.place(x=280,y=170)
    
    average=Checkbutton(feed,text='Average',font=('Showcard Gothic',10),variable=rating,onvalue='Average')
    average.place(x=160,y=200)
    
    poor=Checkbutton(feed,text='Poor',font=('Showcard Gothic',10),variable=rating,onvalue='Poor')
    poor.place(x=280,y=200)
    
    opinion_label=Label(feed, text='How Can We Improve To Serve You Better?',font=('Showcard Gothic',10,'underline'),pady=5)
    opinion_label.place(x=150,y=230)
    
    opinion_box=Text(feed,font=('Showcard Gothic',10),width=38,height=5) 
    opinion_box.place(x=150,y=270)
    #button to submit all data entered
    submit=Button(feed,text='Submit',bg='green',font=('Showcard Gothic',10),command=send,padx=10)
    submit.place(x=240,y=390)
    #button to close window
    close=Button(feed,text='Back',command=feed.destroy,font=('Showcard Gothic',10),padx=5)
    close.place(x=20,y=20)
    
    feed.mainloop()