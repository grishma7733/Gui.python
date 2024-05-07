import sqlite3
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

conn = sqlite3.connect('filename.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users2(filename text NOT NULL)""")

def submit():

    filename = name.get()
    c.execute("INSERT INTO users2 values(?)",(filename,))
    conn.commit()
    


#conn.commit()
#conn.close()


# main window
root=Tk()
root.title("Quickshare")
root.geometry("500x550")
root.configure(bg="white")
root.resizable(False,False)

name = StringVar()

def Send():
   
    window=Toplevel(root)
    window.title("send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        
       
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(('file_type','*.txt'),('all files','*.*')))
        

    def sender():
    
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections...')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        
        print("Data has been sent successfully")
        

    #icon
    
    image_icon1=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\icon.png")
    window.iconphoto(False,image_icon)
    
    
    Sbackground=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\sendback.png")
    Label(window,image=Sbackground,bg='light blue').place(x=0,y=0)

    Mbackground=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\sender.png")
    Label(window,image=Mbackground,bg='aqua').place(x=000,y=200)

    Label(window,text="SEND FILES",font=('georgia',20),bg="#f4fdfe").place(x=160,y=20)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=5,y=70)
    

    Button(window,text='+select file',width=10,height=1,font='arial 14 bold',bg='#fff',fg='#000',command=select_file).place(x=150,y=130)
    Button(window,text='SEND',width=8,height=1,font='arial 14 bold',bg='#000',fg='#fff',command=sender).place(x=300,y=130)

    Label(window,text="Enter file name:",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=200)
    incoming_file=Entry(window,textvariable=name,width=25,fg="black",border=2,bg="white",font=('arial',15))
    incoming_file.place(x=20,y=225)
    Button(window,text='submit',width=8,height=1,font='arial 14 bold',bg='#000',fg='#fff',command=submit).place(x=308,y=218)

    window.mainloop()

def Receive():
   
    main=Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
       
        filename = name.get()
        c.execute("INSERT INTO users2 values(?)",(filename,))
        conn.commit()

        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080 
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        
        print("File has been received succesfully")

    #icon
    image_icon1=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\icon.png")
    main.iconphoto(False,image_icon)

    Hbackground=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\recieveback.png")
    Label(main,image=Hbackground).place(x=190,y=200)
    

    Gbackground=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\sendback.png")
    Label(main,image=Gbackground,bg='#f4fdfe').place(x=0,y=0)


    logo=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\profilepic.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=200,y=100 )

    Label(main,text="Recieve",font=('arial',20),bg="white").place(x=180,y=30)
    
    Label(main,text="Input Sender ID:",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=290)
    SenderID=Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    SenderID.place(x=20,y=320)
    SenderID.focus()


    Label(main,text="file name for the incoming file:",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=370)
    incoming_file=Entry(main,textvariable=name,width=25,fg="black",border=2,bg="white",font=('arial',15))
    incoming_file.place(x=20,y=400)

    imageicon=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\receive1.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=450)
    


    main.mainloop()
       

image_icon=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\icon.png")
root.iconphoto(False,image_icon)

'''
Label(root,text="ShareIt",font=("Comic Sans Ms",20,"bold"),bg="#f4fdfe",fg="blue").place(x=65,y=5)'''
Frame(root,width=450,height=4,bg="#f3f5fe").place(x=25,y=55)


send_image=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=65,y=70)


receive_image=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=70)


Label(root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=65,y=170)
Label(root,text="Receive",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=300,y=170)



background=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\bg.png")
Label(root,image=background).place(x=-1,y=220)


leftimg=PhotoImage(file="C:\\Users\\chpan\\OneDrive\\Pictures\\quickshare2.png")
Label(root,image=leftimg,bg="#f4fdfe",bd=0).place(x=160,y=6)











root.mainloop()