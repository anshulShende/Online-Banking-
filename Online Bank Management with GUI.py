from tkinter import*
from tkinter import messagebox as ms

def logout():
    root.destroy()

def Window2():
    ms.showinfo('Success!',
                'Logged in Successfully\n\n')
    name=log_entry1.get()
    anshul.destroy()
    global root
    root=Tk()
    root.geometry("1200x700+50+50")
    root.title("ATV NET BANKING")
    mainlabel=Label(root,text="ATV NET BANKING",
                font="Verdana 32 bold",
                fg="tomato3")
    mainlabel.pack(anchor=NW,padx=4,pady=3)

    result="WELCOME "+name
    display=Label(root,
                font="Verdana 32 bold",
                fg="black")
    display.place(x=600,y=0)
    display['text']=result
    
    x=Button(root,text="MY ACCOUNTS\nSUMMARY",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=4,width=15,
                      bd=3,relief="sunken")
    x.place(x=450,y=120)
    
    y=Button(root,text="FUNDS\nTRANSFER",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=4,width=15,
                      bd=3,relief="sunken")
    y.place(x=651,y=120)

    Z=Button(root,text="BILL\nPAYMENTS",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=4,width=15,
                      bd=3,relief="sunken")
    Z.place(x=450,y=245)

    H=Button(root,text="MOBILE\nRECHARGE",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=4,width=15,
                      bd=3,relief="sunken")
    H.place(x=651,y=245)

    m=Button(root,text="MINI STATEMENT",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=32,
                      bd=3,relief="sunken")
    m.place(x=450,y=370)

    n=Button(root,text="CHANGE PASSWORD",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=32,
                      bd=3,relief="sunken")
    n.place(x=450,y=445)

    o=Button(root,text="LOG OUT",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=32,
                      bd=3,relief="sunken",
             command=logout)
    o.place(x=450,y=520)

def login():
    label1.place_forget()
    b1.place_forget()
    label2.place_forget()
    b2.place_forget()
    anshul.title("LOGIN PAGE")

    #creating label
    log_label1=Label(anshul,text="NAME",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=25,
                      bd=3,relief="sunken")
    log_label2=Label(anshul,text="PASSWORD",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=25,
                      bd=3,relief="sunken")
    log_label1.place(x=270,y=250)
    log_label2.place(x=270,y=335)
    
    #creating entry
    global log_entry1
    log_entry1=Entry(anshul,bd=5,font = ('',20))
    log_entry2=Entry(anshul,bd=5,font = ('',20),show='*')
    log_entry1.place(x=660,y=260,width=400,height=40)
    log_entry2.place(x=660,y=340,width=400,height=40)
    
   
    #creating checkbox
    log_c=Checkbutton(anshul,text="Keep me logged in",
                      bg="powder blue",font="aerial 16 bold",
                       activebackground="powder blue")
    log_c.place(x=540,y=415)

    log_b1=Button(anshul,text="LOGIN",
                  bg="tomato3",fg="Black",
                      font="aerial 20 bold",
                      height=1,width=25,
                      bd=3,relief="solid",
                 activebackground="powder blue",
                  command=Window2)
    log_b1.place(x=440,y=490)


        
def Registerlogin():
    label1.place_forget()
    b1.place_forget()
    label2.place_forget()
    b2.place_forget()
    anshul.title("LOGIN PAGE")

    
    label.pack_forget()
    regwlabel1.place_forget()
    regwlabel2.place_forget()
    regwentry1.place_forget()
    regwentry2.place_forget()
    regwlabel3.place_forget()
    regwlabel4.place_forget()
    regwentry4.place_forget()
    regwentry3.place_forget()
    regwrad2.place_forget()
    regwrad1.place_forget()
    check.place_forget()
    final.place_forget()

    ms.showinfo('Success!',
                'Signed in Successfully\n\nLogin to Continue')
    
    #creating label
    log_label1=Label(anshul,text="NAME",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=25,
                      bd=3,relief="sunken")
    log_label2=Label(anshul,text="PASSWORD",
                      bg="tomato3",fg="Black",
                      font="aerial 15 bold",
                      height=2,width=25,
                      bd=3,relief="sunken")
    log_label1.place(x=270,y=250)
    log_label2.place(x=270,y=335)
    
    #creating entry
    global log_entry1
    log_entry1=Entry(anshul,bd=5,font = ('',20))
    log_entry2=Entry(anshul,bd=5,font = ('',20),show='*')
    log_entry1.place(x=660,y=260,width=400,height=40)
    log_entry2.place(x=660,y=340,width=400,height=40)

    #creating checkbox
    log_c=Checkbutton(anshul,text="Keep me logged in",
                      bg="powder blue",font="aerial 16 bold",
                       activebackground="powder blue")
    log_c.place(x=540,y=415)

    log_b1=Button(anshul,text="LOGIN",
                  bg="tomato3",fg="Black",
                      font="aerial 20 bold",
                      height=1,width=25,
                      bd=3,relief="solid",
                 activebackground="powder blue",
                  command=Window2)
    log_b1.place(x=440,y=490)

   
        

def register():
    label1.place_forget()
    b1.place_forget()
    label2.place_forget()
    b2.place_forget()
    anshul.title("REGISTRATION PAGE")

    #main label
    global label
    label=Label(anshul,text="PLEASE FILL IN YOUR DETAILS",
                 bg="tomato3",fg="Black",
                 font="consolas 27 bold",
                 height=2,width=40,
                 bd=3,relief="solid")
    label.pack()
    
    #creating label 1&2
    global regwlabel1
    global regwlabel2
    regwlabel1=Label(anshul,text="ENTER YOUR NAME",
                      bg="tomato3",fg="Black",
                      height=3,width=25,
                      bd=3,relief="sunken")
    regwlabel2=Label(anshul,text="ENTER BANK ACC NO.",
                      bg="tomato3",fg="Black",
                      height=3,width=25,
                      bd=3,relief="sunken")
    regwlabel1.place(x=100,y=250)
    regwlabel2.place(x=100,y=330)

    #create Entry widgets for 1&2
    global regwentry1
    global regwentry2
    regwentry1=Entry(anshul,bd=5,font = ('',20))
    regwentry1.place(x=350,y=260,width=400,height=40)#10 more in y
    regwentry2=Entry(anshul,bd=5,font = ('',20))
    regwentry2.place(x=350,y=340,width=400,height=40)#10 more in y

    #creating label 3&4
    global regwlabel3
    global regwlabel4
    regwlabel3=Label(anshul,text="PASSWORD",
                      bg="tomato3",fg="Black",
                      height=3,width=25,
                      bd=3,relief="sunken")
    regwlabel4=Label(anshul,text="CONFIRM PASSWORD",
                      bg="tomato3",fg="Black",
                      height=3,width=25,
                      bd=3,relief="sunken")
    regwlabel3.place(x=100,y=410)
    regwlabel4.place(x=100,y=490)

    #create Entry widgets for 3&4
    global regwentry3
    global regwentry4
    regwentry3=Entry(anshul,bd=5,font = ('',20),show='*')
    regwentry3.place(x=350,y=420,width=400,height=40)#10 more in y
    regwentry4=Entry(anshul,bd=5,font = ('',20),show='*')
    regwentry4.place(x=350,y=500,width=400,height=40)#10 more in y

    #creating radiobutton
    global regwrad1
    global regwrad2
    regwrad1=Radiobutton(anshul,text="MALE",value=1,
                          bg="powder blue",
                          font="aerial 16",
                          activebackground="powder blue")
    regwrad2=Radiobutton(anshul,text="FEMALE",value=2,
                          bg="powder blue",
                          font="aerial 16",
                          activebackground="powder blue")
    regwrad1.place(x=800,y=260)
    regwrad2.place(x=900,y=260)

    
    #creating checkbutton
    global check
    check=Checkbutton(anshul,text="ACCEPT LICENSE AGREEMENT",
                      bg="powder blue",font="aerial 16 ",
                       activebackground="powder blue")
    check.place(x=800,y=330)

    #creating Button Register comfirmation
    global final
    final=Button(anshul,text="COMFIRM SIGN UP",
                 bg="tomato3",fg="Black",
                      font="aerial 20 bold",
                      height=1,width=30,
                      bd=3,relief="solid",
                 activebackground="powder blue",
                 command=Registerlogin)
    final.place(x=450,y=600)
  
    

anshul=Tk()


anshul.title("NET BANKING")
anshul.configure(bg="GREY")
anshul.geometry("1200x700+50+50")


mainlabel=Label(anshul,text="ATV NET BANKING",
                font="Verdana 32 bold",bg="powder blue",
                fg="tomato3")
mainlabel.pack(padx=3,pady=20)


label1=Label(anshul,text="NEW REGISTRATION",bg="tomato3",
             fg="Black",height=3,width=20,
             bd=8,relief="ridge",
             font="aerial 22 bold")
label1.place(x=200,y=150)

b1=Button(anshul,text="SIGN IN",bg="tomato3",
          fg="cornsilk",height=2,width=10,
          font="aerial 22 bold",
          activebackground="powder blue",
          command=register)
b1.place(x=280,y=300)

label2=Label(anshul,text="EXISTING USER",bg="tomato3",
             fg="Black",height=3,width=20,
             bd=8,relief="ridge",
             font="aerial 22 bold")
label2.place(x=800,y=150)

b2=Button(anshul,text="LOGIN",bg="tomato3",
          fg="cornsilk",height=2,width=10,
          font="aerial 22 bold",
          activebackground="powder blue",
          command=login)
b2.place(x=900,y=300)


anshul.mainloop()
