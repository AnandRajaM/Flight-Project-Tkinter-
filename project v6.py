from tkinter import *
from tkinter import messagebox
import pickle
import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user="root",password="system",database="flight")
myc = mydb.cursor()
'''myc.execute("create table details(Flightno int, Name varchar(20),Email varchar(20),Gender varchar(20),Age int,Seat int)")'''

root = Tk()
root.title("Login")
root.geometry('925x500')
root.configure(bg = '#fff')
root.resizable(False,False)

img = PhotoImage(file = 'login.png')
Label(root,image =img,bg = 'white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
heading=Label(frame,text='Sign in',fg = '#57a1f8',bg = 'white',font = ('Microsoft TaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

mainv = 0

def cancelrec():
    x= str(entryc.get())
    print(x)
    t = (x,)
    myc.execute("delete from details where email=%s",t)
    mydb.commit()
    messagebox.showinfo("Success!","Succesfully Canceled your booking!")
    cancelf.destroy()
    main_window()
def cancel():
    global cancelf
    global entryc
    window2.destroy()
    cancelf = Tk()  
    cancelf.geometry('500x250')  
    cancelf.title("Cancelation Form")
    labl0 = Label(cancelf, text="Enter Your Email",width=20,font=("bold", 20))  
    labl0.place(x=75,y=53)  
    labl1 = Label(cancelf, text="Email",width=20,font=("bold", 10))  
    labl1.place(x=68,y=120)  
    entryc = Entry(cancelf)  
    entryc.place(x=240,y=120)

    Button(cancelf, text='Check Email',width=20,bg='brown',fg='white',command=cancelrec).place(x=180,y=180) 

def add_form():
    f1 = str(entryf.get())  
    f2 = str(entryf2.get())  
    f3 = str(entryf3.get())  
    f4 = int(entryf4.get()) 
    print(email)
    t=(f1,f2,f3,f4,email)
    myc.execute("update details set name=%s,email=%s,gender=%s,age=%s where email=%s",t)
    mydb.commit()
    messagebox.showinfo("Success","Succesfully Updated Your Info!")
    main_window()
    base3.destroy()

def update_form():
    global email
    c=0
    myc.execute("select Email from details")
    r = myc.fetchall()
    email = str(entryu.get())
    for i in r:
        if  str(i[0]) == str(entryu.get()):
            c+=1
    if c==0:
        messagebox.showerror("Invalid","No Such Email\nPlease book a flight first!")
    if c==1:
        base2.destroy()
        global base3
        global entryf
        global entryf2
        global entryf3
        global entryf4
        base3 = Tk()  
        base3.geometry('500x500')  
        base3.title("Updation Form")
          
        
        labl0 = Label(base3, text="Updation Form",width=20,font=("bold", 20))  
        labl0.place(x=90,y=53)  

        labl1 = Label(base3, text="FullName",width=20,font=("bold", 10))  
        labl1.place(x=80,y=130)  
        
        entryf = Entry(base3)  
        entryf.place(x=240,y=130)  
        
        labl2 = Label(base3, text="Email",width=20,font=("bold", 10))  
        labl2.place(x=68,y=180)  
        
        entryf2 = Entry(base3)  
        entryf2.place(x=240,y=180)  
        
        labl_3 = Label(base3, text="Gender",width=20,font=("bold", 10))  
        labl_3.place(x=70,y=230) 

        entryf3 = Entry(base3)
        entryf3.place(x=240,y=230)   
        
        labl_4 = Label(base3, text="Age:",width=20,font=("bold", 10))  
        labl_4.place(x=70,y=280)  
        
        entryf4 = Entry(base3)  
        entryf4.place(x=240,y=280)  
        
        Button(base3, text='Submit',width=20,bg='brown',fg='white',command=add_form).place(x=180,y=380)
def display_details():
    global base5
    base5 = Tk()
    base5.title("Current Bookings")
    base5.geometry('925x500')
    base5.configure(bg = '#141414')
    base5.resizable(False,False)
    t=(entryc.get(),)
    myc.execute("select * from details where email=%s",t)
    L = myc.fetchall()
    frame = Frame(base5,width=1000,height=1000,bg='#141414')
    frame.place(x=100,y=30)
    heading=Label(frame,text='Current Bookings',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',23,'bold'))
    heading.place(x=238,y=5)
    heading=Label(frame,text='Flight 1',fg = '#ADD8E6',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=90)
    for i in L:
        heading=Label(frame,text=i[0],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=120)
        heading=Label(frame,text=i[1],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=150)
        heading=Label(frame,text=i[2],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=180)
        heading=Label(frame,text=i[3],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=210)
        heading=Label(frame,text=i[4],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=240)
        heading=Label(frame,text=i[5],fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
        heading.place(x=0,y=270)
        
def current():
    global entryc
    window2.destroy()
    base4 = Tk()
    base4.geometry('500x250')  
    base4.title("Current Bookings")
    labl0 = Label(base4, text="Enter Your Email",width=20,font=("bold", 20))  
    labl0.place(x=75,y=53)  
    labl1 = Label(base4, text="Email",width=20,font=("bold", 10))  
    labl1.place(x=68,y=120)  
    entryc = Entry(base4)  
    entryc.place(x=240,y=120)
    Button(base4, text='Check Email',width=20,bg='brown',fg='white',command=display_details).place(x=180,y=180) 

    
def update():
    global base2
    global entryu
    window2.destroy()
    base2 = Tk()  
    base2.geometry('500x250')  
    base2.title("Contact Form")
    labl0 = Label(base2, text="Enter Your Email",width=20,font=("bold", 20))  
    labl0.place(x=75,y=53)  
    labl1 = Label(base2, text="Email",width=20,font=("bold", 10))  
    labl1.place(x=68,y=120)  
    entryu = Entry(base2)  
    entryu.place(x=240,y=120)

    Button(base2, text='Check Email',width=20,bg='brown',fg='white',command=update_form).place(x=180,y=180) 

def book():
    global windowb
    window2.destroy()
    windowb = Tk()
    windowb.title("Zoop Booking")
    windowb.geometry('925x500')
    windowb.configure(bg = '#141414')
    windowb.resizable(False,False)

    frame = Frame(windowb,width=1000,height=1000,bg='#141414')
    frame.place(x=100,y=30)
    heading=Label(frame,text='Available Flights',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',23,'bold'))
    heading.place(x=238,y=5)

    heading=Label(frame,text='Flight 1',fg = '#ADD8E6',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=90)
    heading=Label(frame,text='Kochi - Bangalore',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=120)
    heading=Label(frame,text='Departure Time: 12:30pm',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=150)
    heading=Label(frame,text='Arrival Time: 1:30am',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=180)
    heading=Label(frame,text='Price: 2000',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=0,y=210)
    
    heading=Label(frame,text='Enter Flight Number and Submit:',fg = '#ADD8E6',bg = '#141414',font = ('Microsoft TaHei UI Light',15,'bold'))
    heading.place(x=185,y=340)


    
    def seat_no(n):
        global mainv
        c=0
        myc.execute("select seat from details")
        r = myc.fetchall()
        print(r)
        for i in r:
            if  i[0] == n:
                c+=1
        if c>=1:
            messagebox.showerror("Invalid","Seat Already Taken!")
        if c==0:
            t1 = (x1,x2,x3,x4,n)
            myc.execute("insert into details values(1549,%s,%s,%s,%s,%s)",t1)
            mydb.commit()
            messagebox.showinfo("Sucess!","Your Flight has been Booked! \n See you on board!")
            main_window()
            seat.destroy()
            
            
    def seats(x,y,text):
        button = Button(seat,text=text,fg='#FF0000',width=2,command=lambda: seat_no(text)).place(x=x,y=y)

    def add_details():
        global x1 , x2 , x3 , x4 
        x1 = str(entry1.get())  #Name
        x2 = str(entry2.get())  #Email
        x3 = str(entry3.get())  #Gender
        x4 = int(entry4.get())  #Age
        ##print("Ok")
        if int(string_f) == 1:
            base.destroy()
            global seat
            seat = Tk()
            seat.geometry('500x500')
            seat.configure(bg = '#141414')

            heading=Label(seat,text='Select Your Seat',fg = '#ffcc66',bg = '#141414',font = ('Microsoft TaHei UI Light',23,'bold'))
            heading.place(x=135,y=8)
            seats(105,100,1)
            seats(125,100,2)
            seats(145,100,3) #sep 50
            seats(195,100,4) #sep 50
            seats(215,100,5)
            seats(235,100,6)
            seats(255,100,7)
            seats(305,100,8)
            seats(325,100,9)
            seats(345,100,10)

            seats(105,126,11)
            seats(125,126,12)
            seats(145,126,13)
            seats(195,126,14)  
            seats(215,126,15)
            seats(235,126,16)
            seats(255,126,17)
            seats(305,126,18)
            seats(325,126,19)
            seats(345,126,20)

            seats(105,152,21)
            seats(125,152,22)
            seats(145,152,23)
            seats(195,152,24)  
            seats(215,152,25)
            seats(235,152,26)
            seats(255,152,27)
            seats(305,152,28)
            seats(325,152,29)
            seats(345,152,30)

            seats(105,178,31)
            seats(125,178,32)
            seats(145,178,33)
            seats(195,178,34)  
            seats(215,178,35)
            seats(235,178,36)
            seats(255,178,37)
            seats(305,178,38)
            seats(325,178,39)
            seats(345,178,40)

            seats(105,250,41)
            seats(125,250,42)
            seats(145,250,43)
            seats(195,250,44)  
            seats(215,250,45)
            seats(235,250,46)
            seats(255,250,47)
            seats(305,250,48)
            seats(325,250,49)
            seats(345,250,50)

            seats(105,276,61)
            seats(125,276,62)
            seats(145,276,63)
            seats(195,276,64)  
            seats(215,276,65)
            seats(235,276,66)
            seats(255,276,67)
            seats(305,276,68)
            seats(325,276,69)
            seats(345,276,70)

            seats(125,302,71)
            seats(145,302,72)
            seats(195,302,73)  
            seats(255,302,74)
            seats(305,302,75)
            seats(325,302,76)

            seats(125,328,77)
            seats(145,328,78)
            seats(195,328,79)  
            seats(255,328,80)
            seats(305,328,81)
            seats(325,328,82)
     
    def ask_data():
        global base
        global entry3
        global entry2
        global entry1
        global entry4
        windowb.destroy()
        base = Tk()  
        base.geometry('500x500')  
        base.title("Contact Form")
          
        
        labl_0 = Label(base, text="Contact Information",width=20,font=("bold", 20))  
        labl_0.place(x=90,y=53)  

        labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
        labl_1.place(x=80,y=130)  
        
        entry1 = Entry(base)  
        entry1.place(x=240,y=130)  
        
        labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
        labl_2.place(x=68,y=180)  
        
        entry2 = Entry(base)  
        entry2.place(x=240,y=180)  
        
        labl_3 = Label(base, text="Gender",width=20,font=("bold", 10))  
        labl_3.place(x=70,y=230) 

        entry3 = Entry(base)
        entry3.place(x=240,y=230)   
        
        labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
        labl_4.place(x=70,y=280)  
        
        entry4 = Entry(base)  
        entry4.place(x=240,y=280)  
        
        Button(base, text='Submit',width=20,bg='brown',fg='white',command=add_details).place(x=180,y=380)   
        base.mainloop()  
       
    def display_text():
        global string_f
        string_f = entryflight.get()
        ask_data()
             
    global entryflight
    entryflight= Entry(windowb, width= 40)
    entryflight.place(x=310,y=405)
    Button(windowb, text= "Submit",width= 20, command= display_text).place(x=360,y=430)

def main_window():
    global window2
    if root.state() != 'normal':
        root.destroy()
    window2 = Tk()
    window2.title("Airline Booking")
    window2.geometry('925x500')
    window2.configure(bg = '#141414')
    window2.resizable(False,False)

    def cbtn(x,y,text,bcolor,fcolor,cmd):
        def on_enter(e):
            mybutton['background']=bcolor
            mybutton['foreground']=fcolor

        def on_leave(e):
            mybutton['background']=fcolor
            mybutton['foreground']=bcolor

        mybutton = Button(window2,width=50,height=10,text=text,fg=bcolor ,bg = fcolor,border = 0 ,activeforeground=fcolor,activebackground=bcolor,command = cmd)

        mybutton.bind("<Enter>",on_enter)
        mybutton.bind("<Leave>",on_leave)
        mybutton.place(x=x,y=y)

    cbtn(50,50,"BOOK A FLIGHT",'#ffcc66','#141414',book)
    cbtn(500,50,"UPDATE INFO",'#ffcc66','#141414',update)
    cbtn(50,250,"CANCEL FLIGHT",'#ffcc66','#141414',cancel)
    cbtn(500,250,"CURRENT BOOKINGS",'#ffcc66','#141414',current)






def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')

def on_enter1(e):
     user1.delete(0, 'end')
def on_leave1(e):
    password=user1.get()
    if password == '':
        user1.insert(0,'Password')

def on_enter3(e):
    user2.delete(0, 'end')
def on_leave3(e):
    name=user2.get()
    if name == '':
        user2.insert(0,'Username')

def on_enter4(e):
     user3.delete(0, 'end')
def on_leave4(e):
    password=user3.get()
    if password == '':
        user3.insert(0,'Password')
    
def signup_final():
    username_signup = user2.get()
    passw_signup = user3.get()

    with open("signin.dat","rb+") as f:
        c= 0 
        while True:
            try:
                x = pickle.load(f)
                username_c = x[0]
                password_c = x[1]
                if username_signup == username_c :
                    messagebox.showerror("Invalid","User Already Exists!")
                    c+=1
            except:
                break


        if c == 0:
            print(username_signup)
            print(passw_signup)
            pickle.dump([str(username_signup),passw_signup],f)
            messagebox.showinfo("Success!","New Account Created!")
            window.destroy()


def signup():
    global photo
    global window
    window = Toplevel()
    window.title("Sign Up")
    window.geometry('925x500')
    window.configure(bg = '#fff')
    window.resizable(False,False)

    photo = PhotoImage(file = 'login2.png')
    label = Label(window,image=photo,bg = 'white').place(x=20,y=50) 
   

    frame = Frame(window,width=350,height=350,bg='white')
    frame.place(x=480,y=70)
    heading=Label(frame,text='Sign up',fg = '#57a1f8',bg = 'white',font = ('Microsoft TaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    
    global user2
    global user3
    user2 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft TaHei UI Light',11))
    user2.place(x=30,y=80)
    user2.insert(0,'Username')
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    user2.bind('<FocusIn>',on_enter3)
    user2.bind('<FocusOut>',on_leave3)

    user3 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft TaHei UI Light',11))
    user3.place(x=30,y=150)
    user3.insert(0,'Password')
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    user3.bind('<FocusIn>',on_enter4)
    user3.bind('<FocusOut>',on_leave4)

    sign_up = Button(frame,width=20,pady = 7,text='Sign up',border= 0 ,bg ='#57a1f8',cursor = 'hand2',fg = 'white',command = signup_final)
    sign_up.place(x=110,y=230)  
  
def signin():
    username=user.get()
    ####print(username)
    password=str(user1.get())
    ####print(password)
    with open("signin.dat","rb") as f:
        c= 0
        while True:
            try:
                x = pickle.load(f)
                username_c = x[0]
                password_c = x[1]
                ####print(username_c)
                ####print(password_c)
                if username == username_c :
                    c+=1
                    if password == str(password_c):
                        main_window()
                    else:
                        messagebox.showerror("Invalid","Invalid Password")
            except EOFError:
                break
        if c == 0 :
             messagebox.showerror("Invalid","No such User!")

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft TaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

user1 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft TaHei UI Light',11))
user1.place(x=30,y=150)
user1.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
user1.bind('<FocusIn>',on_enter1)
user1.bind('<FocusOut>',on_leave1)



Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border = 0,command =signin  ).place(x=35,y=204)
label = Label(frame,text = "Don't have a account?",fg = 'black',bg='white',font = ('Microsoft TaHei UI Light',9))
label.place(x=75,y=270)
sign_up = Button(frame,width=6,text='Sign up',border= 0 ,bg ='white',cursor = 'hand2',fg = '#57a1f8',command = signup)
sign_up.place(x=215,y=270)


root.mainloop()


