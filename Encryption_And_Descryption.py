import tkinter
from tkinter import *
from tkinter import messagebox
import os
import base64

def descrypt():
     password=code.get()
     if password=="1234":
         screen2=Toplevel(screen)
         screen2.title("Encrpytion")
         screen2.geometry("320x430")
         screen2.config(bg="#caa1d1")
         
         message=textbox.get(1.0,END)
         decode_message=message.encode("ascii")
         base64_bytes=base64.b64decode(decode_message)
         decrypt=base64_bytes.decode('ascii')
         
         heading_3=Label(screen2,text="Descrypt",bg='green',fg="#fff",font=("Arial",20))
         heading_3.place(x=20,y=40)
         text_2=Text(screen2,font=('Arial',15),bd=0,relief=GROOVE)
         text_2.place(x=10,y=100,height=100,width=250)
         text_2.insert(END,decrypt)
         
     elif password=="":
          messagebox.showerror("Encryption","input password")
     elif password!="1234":
         messagebox.showerror("Encryption","Invalid Output")
         screen.mainloop()   
def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encrpytion")
        screen1.geometry("320x400")
        screen1.config(bg="#e09f79")
        
        message=textbox.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode('ascii')
        
        heading_3=Label(screen1,text="Encryption",bg='green',fg="#fff",font=("Arial",20))
        heading_3.place(x=20,y=40)
        text_2=Text(screen1,font=('Arial',15),bd=0,relief=GROOVE)
        text_2.place(x=10,y=100,height=100,width=250)
        text_2.insert(END,encrypt)
        
    elif password=="":
         messagebox.showerror("Encryption","input password")
    elif password!="1234":
        messagebox.showerror("Encryption","Invalid Output")
        screen.mainloop()
def main_Screen():
    global code
    global screen
    global textbox
    screen=Tk()
    screen.title("Screte Message for Encryption and Descryption")
    screen.geometry('400x420')
    def reset():
        code.set("")
        textbox.delete(1.0,END)
        
    heading=Label(text="Enter the message for Encrpytion and descyption",fg="black",font=("Arial",10))
    heading.place(x=10,y=30)
    textbox=Text(screen,font=("Arial",14),bg="white",relief=GROOVE,bd=2)
    textbox.place(x=10,y=60,height=100,width=355)
            
    heading_2=Label(screen,text="Enter Screte key for encryption and descryption",fg='black',font=("Arial",10))
    heading_2.place(x=10,y=170)
    code=StringVar()
    entry=Entry(textvariable=code,width=19,bd=0,font=('Arial',20),show="*")
    entry.place(x=10,y=200)

    btn_en=Button(screen,text="Encryption",bg='red',fg='white',font=("Arial",12),command=encrypt)
    btn_en.place(x=30,y=260)


    btn_des=Button(screen,text="Descryption",bg='green',fg='white',font=("Arial",12),command=descrypt)
    btn_des.place(x=200,y=260)

    btn_reset=Button(screen,text='Reset',bg="skyblue",fg='white',font=('Arial',12),bd=2,height=2,width=30,command=reset)
    btn_reset.place(x=10,y=320)
        
    
    screen.mainloop()
    
main_Screen()    
    
    

