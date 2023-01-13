#Teacher Recrutement

#modules
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import sqlite3
import table

#function to update data
def update():
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    #command to update data entered in widgets
    c.execute("""UPDATE teacher SET t_name=:t_name,
t_age=:t_age,
t_gender=:t_gender,
t_exp=:t_exp,
t_encounter=:t_encounter
WHERE t_id="""+e1f2.get(),
              {'t_name':e1f3.get(),
               't_exp':e2f3.get(),
               't_age':age_boxnew.get(),
               't_gender':gendernew.get(),
               't_encounter':c_s_boxnew.get()})
    #to close connection from database
    con.commit()
    con.close()

#function created to delete data from table
def delete():
    #popup to ask y/n to user
    delete=messagebox.askyesno('Delete','Are you sure you want to remove data')
    #ifn answer clicked is yes loop works 
    if delete==1:
        #to connect to database
        con=sqlite3.connect('jujutsu_high_data.db')
        
        c=con.cursor()
        #command to delete data from table of the searched data 
        c.execute('DELETE FROM teacher WHERE t_id='+e1f2.get())
        #to close connection from database
        con.commit()
        con.close()
        #popup to show that the data is succesfully deleted
        succesful=messagebox.showinfo('Delete','Successfully removed Data')
        frame3.destroy()

#function created to search data
def search():
    #button to call function delete
    delete_button=Button(frame2,text='Remove',command=delete,font=10)
    delete_button.grid(row=2,column=0,columnspan=3)
    
    global frame3
    global e1f3
    global e2f3
    global age_boxnew
    global gendernew
    global c_s_boxnew
    #frame created
    frame3=LabelFrame(prince)
    frame3.place(x=100,y=200)
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
        
    c=con.cursor()
    #command to get the searched data
    c.execute('SELECT * FROM teacher WHERE t_id='+e1f2.get())
    #to fetch data searched
    t_data=c.fetchall()
    #print(t_data)
    #to display data fetched in a frame
    for data in t_data:
        print(data)
        #Data
        lb2f3=Label(frame3,text='Name',font=(10))
        lb2f3.grid(row=2,column=0,pady=10)
        
        e1f3=Entry(frame3,font=10)
        e1f3.grid(row=2,column=1)
        e1f3.insert(0,data[1])
        
        lb3f3=Label(frame3,text='ID NO.',font=(10))
        lb3f3.grid(row=1,column=0)
        
        lb4f3=Label(frame3,text=data[0],font=(10),fg='red',bg='light blue',padx=70)
        lb4f3.grid(row=1,column=1)
        
        lb5f3=Label(frame3,text='Experience',font=10)
        lb5f3.grid(row=3,column=0)
        
        e2f3=Spinbox(frame3,from_=0,to=5000,font=10)
        e2f3.grid(row=3,column=1)
        e2f3.delete(0,'end')
        e2f3.insert(0,data[4])
        
        lb6f3=Label(frame3,text='Age',font=10)
        lb6f3.grid(row=4,column=0)
        
        age_boxnew=Spinbox(frame3,from_=0,to=5000,font=10)
        age_boxnew.grid(row=4,column=1,pady=5)
        age_boxnew.delete(0,'end')
        age_boxnew.insert(0,data[2])
        
        lb7f3=Label(frame3,text='Gender',font=10)
        lb7f3.grid(row=5,column=0)

        g=[
            'Male',
            'Female',
            'Others']
        gendernew=StringVar()
        gender_choicenew=OptionMenu(frame3,gendernew,*g)
        gender_choicenew.grid(row=5,column=1)
        gendernew.set(data[3])
        
        c_snew=Label(frame3,text='No. of Encounter \nWith Cursed Spirit:-',font=10)
        c_snew.grid(row=6,column=0)
        c_s_boxnew=Spinbox(frame3,from_=0,to=5000,font=10)
        c_s_boxnew.grid(row=6,column=1,padx=5,pady=5)
        c_s_boxnew.delete(0,'end')
        c_s_boxnew.insert(0,data[5])
        #button to call function update
        b1f3=Button(frame3,text='Update',command=update,font=10,padx=40)
        b1f3.grid(row=7,column=0,columnspan=2,pady=5)
    #to end the connection between the database
    con.commit()
    con.close()

#function to add entered data to database
def join():
    table.create()#to create table if not exists
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
        
    c=con.cursor()
    #command to add data to table
    c.execute('INSERT INTO teacher VALUES (:t_id,:t_name,:t_age,:t_gender,:t_exp,:t_encounter)',
              {'t_id':id_no,
               't_name':e1f1.get(),
               't_exp':e2f1.get(),
               't_age':age_box.get(),
               't_gender':gender.get(),
               't_encounter':c_s_box.get()})
    print(e1f1.get(),id_no,e2f1.get(),age_box.get(),gender.get(),c_s_box.get())
    #to end the connection from database
    con.commit()
    con.close()

#funtion created
def teacher():
    global prince
    #window created 
    prince=Toplevel()
    #title of window
    prince.title('Teacher Recrute')
    #window icon
    prince.iconbitmap('download.ico')
    prince.configure(bg='green')#window background color
    prince.geometry('1005x567')#window size
    
    #window background image
    img=Image.open('teacher_recrute_bg.png')
    bg=ImageTk.PhotoImage(img)
    label = Label(prince, image=bg)
    label.place(x = 0,y = 0)
    
    #button to close window
    back=Button(prince,text='Back',padx=30,command=prince.destroy)
    back.place(x=20,y=20)
    
    global frame1
    global e1f1
    global id_no
    global e2f1
    global age_box
    global gender
    global c_s_box
    #frame created to enter data
    frame1=LabelFrame(prince)
    frame1.place(x=520,y=60)
    #data
    lb1f1=Label(frame1,text='Teacher Recruitement',font=('bold',15),padx=100)
    lb1f1.grid(row=0,column=0,columnspan=3)
        
    lb2f1=Label(frame1,text='Name',font=(10))
    lb2f1.grid(row=2,column=0,pady=10)
    
    e1f1=Entry(frame1,font=10)
    e1f1.grid(row=2,column=1)
    
    lb3f1=Label(frame1,text='ID NO.',font=(10))
    lb3f1.grid(row=1,column=0)
    
    id_no=np.random.randint(1000,10000)
    
    lb4f1=Label(frame1,text=id_no,font=(10),fg='red',bg='light blue',padx=70)
    lb4f1.grid(row=1,column=1)
    
    lb5f1=Label(frame1,text='Experience',font=10)
    lb5f1.grid(row=3,column=0)
    
    e2f1=Spinbox(frame1,from_=0,to=5000,font=10)
    e2f1.grid(row=3,column=1,pady=5)
    
    lb6f1=Label(frame1,text='Age',font=10)
    lb6f1.grid(row=4,column=0)
    
    age_box=Spinbox(frame1,from_=0,to=5000,font=10)
    age_box.grid(row=4,column=1,pady=5)
    
    lb7f1=Label(frame1,text='Gender',font=10)
    lb7f1.grid(row=5,column=0)

    
    g=[
        'Male',
        'Female',
        'Others']
    gender=StringVar()
    gender_choice=OptionMenu(frame1,gender,*g)
    gender_choice.grid(row=5,column=1)
    
    c_s=Label(frame1,text='No. of Encounter With Cursed Spirit:-',font=10)
    c_s.grid(row=6,column=0)
    c_s_box=Spinbox(frame1,from_=0,to=5000,font=10)
    c_s_box.grid(row=6,column=1,padx=5,pady=5)
    #buttons to call function join
    b1f1=Button(frame1,text='Join',command=join,font=10,padx=40)
    b1f1.grid(row=7,column=0,columnspan=2,pady=5)
    
    global frame2
    global e1f2
    #frame created to search data
    frame2=LabelFrame(prince)
    frame2.place(x=100,y=60)
    #to enter data
    lb1f2=Label(frame2,text='Teacher Data',font=('bold',15),padx=100)
    lb1f2.grid(row=0,column=0,columnspan=3)
    
    lb2f2=Label(frame2,text='Teacher ID NO.',font=(10))
    lb2f2.grid(row=1,column=0)
    
    e1f2=Entry(frame2,font=(10))
    e1f2.grid(row=1,column=1)
    #button to call function search
    b1f2=Button(frame2,text='Search',command=search,font=(10))
    b1f2.grid(row=1,column=2,padx=5)
    
    prince.mainloop()