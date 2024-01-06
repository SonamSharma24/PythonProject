import tkinter
from tkinter import *
import datetime

t=tkinter.Tk()
t.title(" Digital Clock")
t.geometry('800x500')
t.config(bg="#b5d5e8")
t.resizable(False,False)

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    minute=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')
    
    label_hour.config(text=hr)
    label_min.config(text=minute)
    label_second.config(text=sec)
    label_am.config(text=am)
    label_date.config(text=date)
    label_month.config(text=month)
    label_year.config(text=year)
    label_day.config(text=day)
    
    label_hour.after(200,date_time)

######### time ##########
label_hour=Label(t,text="00",font=("sans-serif",30,"bold"),bg="#e37562",fg="white")
label_hour.place(x=50,y=30,width=100,height=80)
label_hr_txt=Label(t,text="Hour",font=("bold",20),bg="red",fg="white")
label_hr_txt.place(x=50,y=160,width=100,height=50)

label_min=Label(t,text="00",font=("sans-serif",30,"bold"),bg="#e37562",fg="white")
label_min.place(x=200,y=30,width=100,height=80)
label_min_txt=Label(t,text="Minute",font=("bold",20),bg="red",fg="white")
label_min_txt.place(x=200,y=160,width=100,height=50)

label_second=Label(t,text="00",font=("sans-serif",30,"bold"),bg="#e37562",fg="white")
label_second.place(x=380,y=30,width=100,height=80)
label_second_txt=Label(t,text="second",font=("bold",20),bg="red",fg="white")
label_second_txt.place(x=380,y=160,width=100,height=50)

label_am=Label(t,text="00",font=("sans-serif",30,"bold"),bg="#e37562",fg="white")
label_am.place(x=530,y=30,width=100,height=80)
label_am_txt=Label(t,text="AM/PM",font=("bold",20),bg="red",fg="white")
label_am_txt.place(x=530,y=160,width=100,height=50)

################ Date Month Yaer Day #####

label_date=Label(t,text="00",font=("sans-serif",25,"bold"),bg="#e37562",fg="white")
label_date.place(x=50,y=250,width=100,height=80)
label_date_txt=Label(t,text="Date",font=("bold",20),bg="red",fg="white")
label_date_txt.place(x=50,y=370,width=100,height=50)



label_month=Label(t,text="00",font=("sans-serif",25,"bold"),bg="#e37562",fg="white")
label_month.place(x=200,y=250,width=100,height=80)
label_month_txt=Label(t,text="Month",font=("bold",20),bg="red",fg="white")
label_month_txt.place(x=200,y=370,width=100,height=50)



label_year=Label(t,text="00",font=("sans-serif",25,"bold"),bg="#e37562",fg="white")
label_year.place(x=380,y=250,width=100,height=80)
label_year_txt=Label(t,text="Year",font=("bold",20),bg="red",fg="white")
label_year_txt.place(x=380,y=370,width=100,height=50)



label_day=Label(t,text="00",font=("sans-serif",25,"bold"),bg="#e37562",fg="white")
label_day.place(x=530,y=250,width=100,height=80)
label_day_txt=Label(t,text="Day",font=("bold",20),bg="red",fg="white")
label_day_txt.place(x=530,y=370,width=100,height=50)

date_time()

t.mainloop()

