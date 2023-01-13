#JUJUTSU KAISEN HIGH SCHOOL ,TOKYO
#SITE TO TAKE ADMISION IN HIGH SCHOOL &&
#WIKIPIDEA OF SCHOOL

#modules
from tkinter import *
from PIL import ImageTk,Image
import jujutsu_wiki
import admission
import teacher_recruite
import feedback

#creating window
web=Tk()
#adding title to window
web.title('JUJUTSU KAISEN HIGH SCHOOL')
#adding logo to window
web.iconbitmap('download.ico')
web.configure(bg='#6E6E8B')#background color
web.geometry('555x315')#window geometry

#background image
img =Image.open('jujutsu2.png')
bg = ImageTk.PhotoImage(img)
label = Label(web, image=bg)
label.place(x = 0,y = 0)

#labels
Label(web,text='Jujutsu High Tokyo',padx=30).place(x = 190,y = 215)

#buttons
Button(web,text='Jujutu Kaisen Wiki',bg='red',command=jujutsu_wiki.wiki).place(x = 10,y = 285)
Button(web,text='Jujutu High Admission',command=admission.admission,bg='red').place(x = 10,y = 255)
Button(web,text='Teacher Recruite',command=teacher_recruite.teacher,bg='red').place(x = 452,y = 255)
Button(web,text='Exit',bg='red',padx=30,command=web.destroy).place(x = 465,y = 285)
Button(web,text='Feedback',bg='red',padx=14,command=feedback.feedback).place(x = 465,y = 225)





web.mainloop()