#take a admission in jujutsu high

#modules
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import sqlite3
import table

#function to update values
def set_():
    #connecting to database
    con=sqlite3.connect('jujutsu_high_data.db')
        
    c=con.cursor()
    #command to update values by calling all entered data
    c.execute('''UPDATE admission SET st_name=:st_name,
st_age=:st_age,
st_gender=:st_gender,
st_exp=:st_exp,
st_type=:st_type,
st_encounter=:st_encounter
WHERE st_id='''+search_entry.get(),
              {'st_name':st_name_valuenew.get(),
              'st_age':st_age_valuenew.get(),
              'st_gender':gendernew.get(),
              'st_exp':expnew.get(),
              'st_type':clicknew.get(),
              'st_encounter':st_encounter_valuenew.get()
               })
    #to end connection
    con.commit()
    con.close()

#function to delete
def remove():
    #popup to ask y/n question
    delete=messagebox.askyesno('Delete','Are you sure you want to remove data')
    #loop to delete
    if delete==1:    
        con=sqlite3.connect('jujutsu_high_data.db')
        
        c=con.cursor()
        #command to delete searched data    
        c.execute('DELETE FROM admission WHERE st_id='+search_entry.get())
        #to close connection
        con.commit()
        con.close()
        #popup created
        succesful=messagebox.showinfo('Delete','Successfully removed Data')
        admin.destroy()#to destroy window
        admission()#to run function admission

#function to update the searched data
def update():
    #connection to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    #command to get data searched
    c.execute('SELECT * FROM admission WHERE st_id='+search_entry.get())
    #to fetchall data searched
    records=c.fetchall()
    
    global set_data
    global st_name_valuenew
    global st_age_valuenew
    global gendernew
    global expnew
    global clicknew
    global st_encounter_valuenew
    #creating frame
    set_data=LabelFrame(admin)
    set_data.place(x=370,y=50)
    #data
    for record in records:
        print(record)
        st_no_labelnew=Label(set_data,text='Id No.')
        st_no_labelnew.grid(row=0,column=0,padx=50,pady=5)
        st_no_valuenew=Label(set_data,text=record[0])
        st_no_valuenew.grid(row=0,column=1,padx=50,pady=5)
        
        st_name_labelnew=Label(set_data,text='Name')
        st_name_labelnew.grid(row=1,column=0,padx=50,pady=5)
        st_name_valuenew=Entry(set_data)
        st_name_valuenew.grid(row=1,column=1,padx=50,pady=5)
        st_name_valuenew.insert(0,record[1])
        
        st_age_labelnew=Label(set_data,text='Age')
        st_age_labelnew.grid(row=2,column=0,padx=50,pady=5)
        st_age_valuenew=Spinbox(set_data,from_=0,to=5000)
        st_age_valuenew.grid(row=2,column=1,padx=50,pady=5)
        st_age_valuenew.delete(0,'end')
        st_age_valuenew.insert(0,record[2])
        
        st_gender_labelnew=Label(set_data,text='Gender')
        st_gender_labelnew.grid(row=3,column=0,padx=50,pady=5)
        g=[
            'Male',
            'Female',
            'Others']

        gendernew=StringVar()
        gendernew.set(record[3])
        gender_choice=OptionMenu(set_data,gendernew,*g)
        gender_choice.grid(row=3,column=1,padx=50,pady=5)
        
        st_exp_labelnew=Label(set_data,text='Experience')
        st_exp_labelnew.grid(row=4,column=0,padx=50,pady=5)
        expval=['Fresher',
                'Experience']
        expnew=StringVar()
        expnew.set(record[4])
        st_exp_valuenew=OptionMenu(set_data,expnew,*expval)
        st_exp_valuenew.grid(row=4,column=1,padx=50,pady=5)
        
        st_type_labelnew=Label(set_data,text='Type')
        st_type_labelnew.grid(row=5,column=0,padx=50,pady=5)
        u_t=['Cursed Energy',
             'Cursed Weapon']
        
        clicknew=StringVar()
        clicknew.set(record[5])
        typ_choice=OptionMenu(set_data,clicknew,*u_t)
        typ_choice.grid(row=5,column=1,padx=50,pady=5)
        
        st_encounter_labelnew=Label(set_data,text='Encounter')
        st_encounter_labelnew.grid(row=6,column=0,padx=50,pady=5)
        st_encounter_valuenew=Spinbox(set_data,from_=0,to=5000)
        st_encounter_valuenew.grid(row=6,column=1,padx=50,pady=5)
        st_encounter_valuenew.delete(0,'end')
        st_encounter_valuenew.insert(0,record[6])
        
        st_teacher_labelnew=Label(set_data,text='Teacher')
        st_teacher_labelnew.grid(row=7,column=0,padx=50,pady=5)
        st_teacher_valuenew=Label(set_data,text=record[7])
        st_teacher_valuenew.grid(row=7,column=1,padx=50,pady=5)
        
        #button to set all changed data 
        setval=Button(set_data,text='Set',command=set_,padx=30,pady=5)
        setval.grid(row=8,column=0,columnspan=2,padx=50,pady=5)
        
    con.commit()
    con.close()
    
#function to search details of students
def search():
    sensei_frame.destroy()#to destroy frame
    form.destroy()#to destroy frame
    print(search_entry.get())
    #buttons
    update_button=Button(list_frame,text='Update',command=update,padx=20,pady=3)
    update_button.place(x=130,y=47)
    remove_button=Button(list_frame,text='Remove',command=remove,padx=10,pady=3)
    remove_button.grid(row=2,column=0,columnspan=2,padx=10)
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    #execute to find details of selected students
    c.execute('SELECT * FROM admission WHERE st_id='+search_entry.get())
    #to fetch execute command
    records=c.fetchall()
    
    #new frame to display searched data
    global st_data
    st_data=LabelFrame(admin,padx=50)
    st_data.place(x=50,y=150)
    for record in records:
        print(record)
        #data searched
        st_no_label=Label(st_data,text='Id No.')
        st_no_label.grid(row=0,column=0,padx=10,pady=5)
        st_no_value=Label(st_data,text=record[0])
        st_no_value.grid(row=0,column=1,padx=10,pady=5)
        
        st_name_label=Label(st_data,text='Name')
        st_name_label.grid(row=1,column=0,padx=10,pady=5)
        st_name_value=Label(st_data,text=record[1])
        st_name_value.grid(row=1,column=1,padx=10,pady=5)
        
        st_age_label=Label(st_data,text='Age')
        st_age_label.grid(row=2,column=0,padx=10,pady=5)
        st_age_value=Label(st_data,text=record[2])
        st_age_value.grid(row=2,column=1,padx=10,pady=5)
        
        st_gender_label=Label(st_data,text='Gender')
        st_gender_label.grid(row=3,column=0,padx=10,pady=5)
        st_gender_value=Label(st_data,text=record[3])
        st_gender_value.grid(row=3,column=1,padx=10,pady=5)
        
        st_exp_label=Label(st_data,text='Experience')
        st_exp_label.grid(row=4,column=0,padx=10,pady=5)
        st_exp_value=Label(st_data,text=record[4])
        st_exp_value.grid(row=4,column=1,padx=10,pady=5)
        
        st_type_label=Label(st_data,text='Type')
        st_type_label.grid(row=5,column=0,padx=10,pady=5)
        st_type_value=Label(st_data,text=record[5])
        st_type_value.grid(row=5,column=1,padx=10,pady=5)
        
        st_encounter_label=Label(st_data,text='Encounter')
        st_encounter_label.grid(row=6,column=0,padx=10,pady=5)
        st_encounter_value=Label(st_data,text=record[6])
        st_encounter_value.grid(row=6,column=1,padx=10,pady=5)
        
        st_teacher_label=Label(st_data,text='Teacher')
        st_teacher_label.grid(row=7,column=0,padx=10,pady=5)
        st_teacher_value=Label(st_data,text=record[7])
        st_teacher_value.grid(row=7,column=1,padx=10,pady=5)
        
    #to close the connection    
    con.commit()
    con.close()
    #to close frame if exists
    try:
        sensei_selected_frame.destroy()
    except:
        return

#function to add data in database
def add():
    table.create()
    #to connect to database
    con=sqlite3.connect('jujutsu_high_data.db')
    
    c=con.cursor()
    '''If selected 'Experienced' choice button
       it takes in the entered data of experience
       else,
       it takes in the value as null'''
    if e=='Experienced':
        encounter=c_s_box.get()
    else:
        encounter='NULL'
    print(encounter)
    
    #execute to add data in the table by calling the entered data 
    c.execute('INSERT INTO admission VALUES (:st_id,:st_name,:st_age,:st_gender,:st_exp,:st_type,:st_encounter,:st_teacher)',
              {'st_id':id_no,
              'st_name':name_box.get(),
              'st_age':age_box.get(),
              'st_gender':gender.get(),
              'st_exp':enter.get(),
              'st_type':click.get(),
              'st_encounter':encounter,
              'st_teacher':selected
               })
    
    c.execute('SELECT * FROM admission')
    data=c.fetchall()
    for i in data:
        print(i)
    #to close the connection
    con.commit()
    con.close()

#function to select a random teacher
def sensei():
    global e
    global selected
    #all teachers name and their images are in list
    senseis=['Satoru Gojo','Atsuya Kusakabe','Kiyotaka Ijichi','Shoka leiri','Akari Nitta','Masanichi Yaga']
    sensei_img=['gojo.png','AtsuyaKusakabe.png','Ijichi.png','ShokoIeri.png','AkariNitta.png','Masamichi.png']
    #random number is generated from given range
    num=np.random.randint(0,6)
    print(num)
    #using number list is sliced and teacher is selected
    selected=senseis[num]
    print(selected)
    
    global sensei_selected_frame
    #frame created to display selected teacher
    sensei_selected_frame=LabelFrame(admin,padx=72)
    sensei_selected_frame.place(x=400,y=300)
    Label(sensei_selected_frame,text='Your Selected Teacher',font=('Arial',10,'bold')).grid(row=0,column=0,columnspan=3)    
    img=ImageTk.PhotoImage(Image.open(sensei_img[num]))
    pic=Label(sensei_selected_frame,image=img)
    pic.grid(row=1,column=0)
    Label(sensei_selected_frame,text=selected).grid(row=1,column=1)
    #to disable the button
    press=Button(form,text='Press, To Select a Sensei',state=DISABLED,padx=20).grid(row=7,column=0,columnspan=2,pady=10)
    #pop created to show selected teacher
    popup=messagebox.showinfo('Your Selected Teacher',selected+'            ')
    
    e=(enter.get())
    if e=='Experienced':
        global lf
        global c_s_box
        lf=LabelFrame(form)
        lf.grid(row=8,column=0,columnspan=2)
        c_s=Label(lf,text='No. of Encounter With Cursed Spirit')
        c_s.pack()
        c_s_box=Spinbox(lf,from_=0,to=5000)
        c_s_box.pack()
        sensei_selected_frame.place(x=400,y=350)
    
    
    if e=='Fresher':
        try:
            lf.destroy()
        except:
            return

    if e==0:
        try:
            lf.destroy()
        except:
            return

#function admission
def admission():
    #creating a window
    global admin
    admin=Toplevel()
    #window title
    admin.title('Jujutu High Admission')
    #window icon
    admin.iconbitmap('download.ico')
    admin.configure(bg='yellow')#background color
    admin.geometry('800x450')#window size
    
    #background image
    img=Image.open('admission.png')
    bg=ImageTk.PhotoImage(img)
    label = Label(admin, image=bg)
    label.place(x = 0,y = 0)
    
    global form
    global sensei_frame
    global search_entry
    global list_frame
    #creating frame
    form=LabelFrame(admin)
    form.place(x=400,y=30)
    
    #back button
    #to close the window
    back=Button(admin,text='Back',command=admin.destroy,padx=20)
    back.place(x=50,y=20)
    
#     creating frame
    list_frame=LabelFrame(admin)
    list_frame.place(x=50,y=50)
    #data in frame
    list_label=Label(list_frame,text='Student Data')
    list_label.grid(row=0,column=0,columnspan=3)
    
    search_label=Label(list_frame,text='ID NO.')
    search_label.grid(row=1,column=0)
    
    search_entry=Entry(list_frame)
    search_entry.grid(row=1,column=1)
    
    #creating frame
    sensei_frame=LabelFrame(admin,padx=50)
    sensei_frame.place(x=50,y=120)
    #button
    search_Button=Button(list_frame,text='Student List',command=search)
    search_Button.grid(row=1,column=2,padx=5)
    """All teachrs name and
       All teachers images
       are in list.
       They are Displayed in frame."""
    senseis=['Satoru Gojo','Atsuya Kusakabe','Kiyotaka Ijichi','Shoka leiri','Akari Nitta','Masamichi Yaga']
    sensei_img=['gojo.png','AtsuyaKusakabe.png','Ijichi.png','ShokoIeri.png','AkariNitta.png','Masamichi.png']
    for i in range(0,6):
        Label(sensei_frame,text=senseis[i]).grid(row=i,column=1)
    #to diaplay images
    img1=ImageTk.PhotoImage(Image.open(sensei_img[0]))
    pic1=Label(sensei_frame,image=img1)
    pic1.grid(row=0,column=0)
    
    img2=ImageTk.PhotoImage(Image.open(sensei_img[1]))
    pic2=Label(sensei_frame,image=img2)
    pic2.grid(row=1,column=0)
    
    img3=ImageTk.PhotoImage(Image.open(sensei_img[2]))
    pic3=Label(sensei_frame,image=img3)
    pic3.grid(row=2,column=0)
    
    img4=ImageTk.PhotoImage(Image.open(sensei_img[3]))
    pic4=Label(sensei_frame,image=img4)
    pic4.grid(row=3,column=0)
    
    img5=ImageTk.PhotoImage(Image.open(sensei_img[4]))
    pic5=Label(sensei_frame,image=img5)
    pic5.grid(row=4,column=0)
    
    img6=ImageTk.PhotoImage(Image.open(sensei_img[5]))
    pic6=Label(sensei_frame,image=img6)
    pic6.grid(row=5,column=0)
    
    global id_no
    global name_box
    global age_box
    global gender
    global enter
    global click
    #data of frame 'form'
    title=Label(form,text='Admission Form',padx=100)
    title.grid(row=0,column=0,columnspan=2)
    
    id_label=Label(form,text='ID NO.')
    id_label.grid(row=1,column=0)
    #id no is generated
    id_no=np.random.randint(1000,10000)
    
    id_no_label=Label(form,text=id_no,fg='red',bg='light blue',padx=70)
    id_no_label.grid(row=1,column=1)
       
    name_label=Label(form,text='Name')
    name_label.grid(row=2,column=0)
    
    name_box=Entry(form,width=30)
    name_box.grid(row=2,column=1)
    
    age_label=Label(form,text='Age')
    age_label.grid(row=3,column=0)
    
    age_box=Spinbox(form,from_=0,to=5000)
    age_box.grid(row=3,column=1)
    
    gender_label=Label(form,text='Gender')
    gender_label.grid(row=4,column=0)
    
    g=[
        'Male',
        'Female',
        'Others']

    gender=StringVar()
    gender_choice=OptionMenu(form,gender,*g)
    gender_choice.grid(row=4,column=1)
    
    enter=StringVar()
    fress=Checkbutton(form,text='Fresher',variable=enter,onvalue='Fresher',offvalue='0')
    fress.deselect()
    fress.grid(row=5,column=0)
    
    exp=Checkbutton(form,text='Experienced',variable=enter,onvalue='Experienced',offvalue='0')
    exp.deselect()
    exp.grid(row=5,column=1)

    typ=Label(form,text='Type of user:')
    typ.grid(row=6,column=0)
    
    u_t=['Cursed Energy',
         'Cursed Weapon']
    
    click=StringVar()
    typ_choice=OptionMenu(form,click,*u_t)
    typ_choice.grid(row=6,column=1)
    
    global press
    #button to generate random selection of teacher
    press=Button(form,text='Press, To Select a Sensei',command=sensei,padx=20).grid(row=7,column=0,columnspan=2,pady=10)
    #button to add data in database
    Button(form,text='Done',command=add,padx=20).grid(row=9,column=0,columnspan=2,pady=10)
    
    admin.mainloop()