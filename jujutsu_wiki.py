#wiki of jujutsu high tokyo

#modules
from tkinter import *
from PIL import ImageTk,Image

#funstion to show wiki page of jujutsu high tokyo
def wiki():
    #to create window
    wiki=Toplevel()
    #title of window
    wiki.title('JUJUTSU KAISEN WIKI')
    #window icon
    wiki.iconbitmap('download.ico')
    wiki.configure(bg='red')#window background colur
    wiki.attributes('-fullscreen',True)#to open window in full size
    
    #Data
    """Data contains all types of png images and text """
    img =Image.open('Capture.png')
    bg = ImageTk.PhotoImage(img)
    label = Label(wiki, image=bg)
    label.place(x = 0,y = 0)
    
    #frame create 
    frame1=LabelFrame(wiki)
    #back button to close the window
    back=Button(wiki,text='Back',padx=20,command=wiki.destroy)
    back.place(x=50,y=20)
    #canvas created in frame to make data of frame scroll able
    mycanvas=Canvas(frame1)
    mycanvas.pack(side=LEFT,fill='both',expand='yes')
    #scrollbar
    yscroll=ttk.Scrollbar(mycanvas,orient='vertical',command=mycanvas.yview)
    yscroll.pack(side='right',fill='y')
    #frame created canvas to make the scroll
    myframe=Frame(mycanvas)
    mycanvas.create_window((0,0),window=myframe,anchor='nw')

    mycanvas.config(yscrollcommand=yscroll.set)


    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    frame1.pack(fill='both',expand='yes',padx=50,pady=50)
    
    pic=ImageTk.PhotoImage(Image.open('Capture2.png'))
    my_Label=Label(myframe,image=pic)
    my_Label.grid(row=0,column=0,pady=5,padx=10)
    
#     title=Label(myframe,text='Jujutsu Kaisen Wiki',font=("Arial", 25))
#     title.grid(row=0,column=1,pady=5)
    
    intro=Label(myframe,text="Tokyo Prefectural Jujutsu High School (東とう京きょう都と立り\nつ呪じゅ術じゅつ高こう等とう専せん門もん学がっ校こう\nTōkyō Toritsu Jujutsu Kōtō Senmon Gakkō?, lit. Tokyo Metropolitan \nCurse Technical College), commonly referred to as Tokyo Jujutsu High, \nis one of only two jujutsu educational institutions in Japan dedicated to \nfostering the next generation of jujutsu sorcerers.",font=('Arial',15))
    intro.grid(row=2,column=0)
    
    pic2=ImageTk.PhotoImage(Image.open('jujutsu tokyo.png'))
    build=Label(myframe,image=pic2)
    build.grid(row=2,column=1)
    
    disc_title=Label(myframe,text="Description                                                                                    \n",font=('Arial',15,'underline'),foreground='grey')
    disc_title.grid(row=3,column=0)
    
    disc=Label(myframe,text="Tokyo Jujutsu High serves not only as a training ground for the next generation \nof sorcerers but a headquarters for all alumni who have graduated on to \nbe full-fledged jujutsu sorcerers as well. All sorcerers play a \nrole in mentoring jujutsu students, whether in a teacher's role \nor accompanying them on missions. Weaker sorcerers are assigned the \nroles of windows, someone who can see curses but is not considered \na full-fledged sorcerer or managers to contribute as well.\n\nThe jujutsu schools are considered the place for the community and \nprovide mediation, general support, education, and shelter.\n\n",font=('Arial',15)) 
    disc.grid(row=4,column=0)
    
    pic3=ImageTk.PhotoImage(Image.open('tokyo jujutsu high logo.png'))
    build=Label(myframe,image=pic3)
    build.grid(row=4,column=1)
    
    location_title=Label(myframe,text='Location                                                                                     \n',font=('Arial',15,'bold'),foreground='black')
    location_title.grid(row=5,column=0)
    
    location=Label(myframe,text="Tokyo Jujutsu High is a broad campus of several buildings build in a traditional Japanese architectural style, operating  \nunder the guise of a Buddhist temple. The school building is well hidden on Tokyo's outskirts, far and high in the \nmountains. Naturally, there are a lot of trees around the property to further obscure the location. Some elements other than the \nbuildings reflect the Buddhist theme. There are several statues of deities, shrines, and torii gates around the campus.\n \nThere are several entrances into the school. The entire property is hidden by a protective barrier maintained by Master \nTengen, who lives beneath the school in the star's underground tombs. The school grounds include training grounds, \ncourtyards, dormitories, and classrooms, among a variety of other amenities.\n",font=('Arial',15))
    location.grid(row=6,column=0,columnspan=2)
    
    pic4=ImageTk.PhotoImage(Image.open('high school.png'))
    build=Label(myframe,image=pic4)
    build.grid(row=7,column=0)
    
    pic5=ImageTk.PhotoImage(Image.open('drone_site.png'))
    build=Label(myframe,image=pic5)
    build.grid(row=7,column=1)
    
    admins_title=Label(myframe,text='\n\nAdministration                                                                                  \n',font=('Aria',15,'bold'),fg='black')
    admins_title.grid(row=8,column=0)
    
    admins1=Label(myframe,text="""The members of authority at Jujutsu High are known as the "higher-ups". The higher-ups control the majority \nof decisions revolving around the school. They hold their meetings in a dimly lit room with \na single light that illuminates whoever is speaking to the board. The higher-ups' bodies are \nhidden from view using doors that stand on their own. Their members consists of older men like \nKyoto Principal, Yoshinobu Gakuganji.\n""",font=('Arial',15))
    admins1.grid(row=9,column=0,columnspan=2)
    
    admins2=Label(myframe,text="""They are conservative traditionalists that often clash with those that have progressive ambition like Satoru Gojo. \nMany of the politics involved with governing the jujutsu community effects the school and its students. \nBoth Yuta Okkotsu and Yuji Itadori were isolated on campus in sealed rooms and initially scheduled for \nexecution. Even after being vouched for by Satoru Gojo, both students, who enrolled at two different\n times, have only had their executions suspended since. """,font=('Arial',15))
    admins2.grid(row=10,column=0,columnspan=2)
    
    r_stitle=Label(myframe,text='\n\nRules and Security                                                                        ',font=('Arial',15,'bold'))
    r_stitle.grid(row=11,column=0)
    
    r_s1=Label(myframe,text="""\nUpon enrolling in Jujutsu High, transfer students are taught about the school's rules and \nsecurity measures. The school is protected by Master Tengen's barrier, which hides its \nlocation from the outside world. Those who already know the location can easily find it. One entrance \nis in the foothills of Mount Mushiro up a long set of stairs marked with a series of torii gates.\n""",font=('Arial',15))
    r_s1.grid(row=12,column=0,columnspan=2)
    
    r_s2=Label(myframe,text="""All jujutsu sorcerers must abide by jujutsu regulations. There appear to be \nseveral articles, most of which have not been revealed. They call for someone's \nimmediate execution even if they become a potential vessel to a curse as powerful as Sukuna.\n Article 9 of the jujutsu regulations punishes jujutsu sorcerers turned curse users with \nexecution as well. """,font=('Arial',15,))
    r_s2.grid(row=13,column=0,columnspan=2)
    
    circumtitle=Label(myframe,text='Curriculum                                                                                       ',font=('Arial',15,'underline'),foreground='grey')
    circumtitle.grid(row=14,column=0)
    
    circum1=Label(myframe,text="""\nThe school's curriculum is taught over four years. The concept is to train young sorcerers \nto control their curses and use them to exorcise other curses. All classes appear to be taught \nby active professional jujutsu sorcerers. The teachers regulate their students' training regiments \nand education as they see fit. Sorcerers are rare, so classes are often small and focused on building up \nthe individual students into competent sorcerers as quickly as possible.""",font=('Arial',15))
    circum1.grid(row=15,column=0,columnspan=2)
    
    circum2=Label(myframe,text=""" \nStudents are given a formal education with standard school \nclasses such as homeroom and sorcerer training through \npractical jujutsu classes. They move from their original \nhomes to live on campus in the dormitories. The majority \nof training, classes, and school events are \nall conducted on campus grounds.""",font=('Arial',15))
    circum2.grid(row=16,column=0)
    
    pic6=ImageTk.PhotoImage(Image.open('pic6.png'))
    circum_img=Label(myframe,image=pic6)
    circum_img.grid(row=16,column=1)
    
    circum3=Label(myframe,text="""\nPractical training assignments and field tests often consist of investigating paranormal locations and exorcising \nweaker curses. Jujutsu High students are ranked on the same scale as professional jujutsu sorcerers, which their \nstudent ID reflects. Same as jujutsu sorcerers, students are given missions according to their ranking. When leaving \nschool grounds to exorcise curses as a part of their training to gain experience, students are often \nsupervised by a sorcerer or manager.""",font=('Arial',15))
    circum3.grid(row=17,column=0,columnspan=2)
    
    uni_title=Label(myframe,text='Uniforms                                                                                         \n',font=('Arial',15,'underline'),fg='grey')
    uni_title.grid(row=18,column=0)
    
    uni1=Label(myframe,text="""The male school uniform consists of asymmetrical blue jackets with high collars and two pins on the left side \nengraved with the school logo. The male uniform is completed with a pair of matching blue slacks. The standard \nfemale uniform has the same top with a skirt for a bottom.""",font=('Arial',15))
    uni1.grid(row=19,column=0,columnspan=2)
    
    uni2=Label(myframe,text="""\nThe uniforms are highly customizable, and many of the students have their own variations of the uniform. \nThe top half of Nobara's uniform is similar to a traditional gakuran uniform, with buttons from top to bottom down \nthe middle. Yuta's uniform is all white, and Yuji's uniform is customized with a hood as one of many \npossible examples. """,font=('Arial',15))
    uni2.grid(row=20,column=0,columnspan=2)
    
    uni3=Label(myframe,text="""\nJujutsu High has summer and winter uniforms like most Japanese schools. There usually isn't much difference between \nthem other than breathability because the uniforms must remain practical for combat. If a student desires a custom \nuniform, they can put in a request with the school.""",font=('Arial',15))
    uni3.grid(row=21,column=0,columnspan=2)
    
    pic7=ImageTk.PhotoImage(Image.open('pic7.png'))
    uni_img=Label(myframe,image=pic7)
    uni_img.grid(row=22,column=0, columnspan=2)
    
    sc_ev_title=Label(myframe,text='School Events                                                                                 ',font=('Arial',15,'underline'),fg='grey')
    sc_ev_title.grid(row=23,column=0)
    
    sc_ev=Label(myframe,text="""\nKyoto Sister-School Goodwill Event: Tokyo and Kyoto students participate in a joint annual competition to promote \ngoodwill between the sister schools. The competition takes place on the campus of the previous year's winner. \nThe principals of both schools decide on two competitions for the students centered around jujutsu battles. \nTraditionally there is always a team competition and an individual competition. """,font=('Arial',15))
    sc_ev.grid(row=24,column=0,columnspan=2)
    
    la_title=Label(myframe,text='\nLandmarks                                                                                         ',font=('Arial',15,'underline'),fg='grey')
    la_title.grid(row=25,column=0)
    
    pic8=ImageTk.PhotoImage(Image.open('pic8.png'))
    la_img1=Label(myframe,image=pic8)
    la_img1.grid(row=26,column=0, columnspan=2)
    
    pic9=ImageTk.PhotoImage(Image.open('pic9.png'))
    la_img2=Label(myframe,image=pic9)
    la_img2.grid(row=27,column=0, columnspan=2)
    
    pic10=ImageTk.PhotoImage(Image.open('pic10.png'))
    la_img3=Label(myframe,image=pic10)
    la_img3.grid(row=28,column=0, columnspan=2)
    
    s_s_title=Label(myframe,text='\nStaff & Students                                                                             ',font=('Arial',15,'underline'),fg='grey')
    s_s_title.grid(row=29,column=0)
    
    pic11=ImageTk.PhotoImage(Image.open('pic11.png'))
    s_s_img1=Label(myframe,image=pic11)
    s_s_img1.grid(row=30,column=0, columnspan=2)
    
    pic12=ImageTk.PhotoImage(Image.open('pic12.png'))
    s_s_img2=Label(myframe,image=pic12)
    s_s_img2.grid(row=31,column=0, columnspan=2)
    
    n_title=Label(myframe,text='\nNavigation                                                                                    \n',font=('Arial',15,'underline'),fg='grey')
    n_title.grid(row=32,column=0)
    
    pic13=ImageTk.PhotoImage(Image.open('pic13.png'))
    n_img1=Label(myframe,image=pic13)
    n_img1.grid(row=33,column=0, columnspan=2)
    
    wiki.mainloop()