import tkinter
from tkinter import *
from textblob import TextBlob
t=tkinter.Tk()

t.title("Spelling checker")
t.geometry('500x400')
t.config(bg="#9c7391")
t.resizable(False,False)

global incorrect_entry,correct_entry
def correct_spelling():
    get_data=incorrect_entry.get()
    corr=TextBlob(get_data)
    data=corr.correct()
    correct_entry.delete(0,END)
    correct_entry.insert(0, data)
    
    

### incorrect label ####
incorrect_label=Label(t,text="Incorrect word",font=('bold',20),bg="red",fg="white")
incorrect_label.place(x=120,y=30)

incorrect_entry=Entry(t,width=20,font=('bold',20))
incorrect_entry.place(x=120,y=90)

correct_label=Label(t,text="Correct word",font=('bold',20),bg="red",fg="white")
correct_label.place(x=120,y=150)
correct_entry=Entry(t,width=20,font=('bold',20))
correct_entry.place(x=120,y=210)

btn=Button(t,text='Done',font=('bold',15),fg="white",bg='green',width=15,command=correct_spelling)
btn.place(x=150,y=280)
t.mainloop()

#obj=TextBlob("comptr")

#print(obj.correct())




















