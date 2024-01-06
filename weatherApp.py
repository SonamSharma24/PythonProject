import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import requests
t=tkinter.Tk()
t.title("Weather App")
t.geometry("700x650")
t.resizable(False,False)

city_name=StringVar()


def get_data():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b9c82f500219b8735fb4579badb8cfd9").json()
    wl.config(text=data["weather"][0]["main"])
    wd.config(text=data['weather'][0]["description"])
    temperature.config(text=str(int(data["main"]['temp']-273.15)))
    per.config(text=data['main']["pressure"])
    
    
    
#### weather app image #####



w1=Label(t,text="Weather App",font=("sans-serif",30,'bold'),bg="#ab6591",fg='white',bd=2,relief=RIDGE)
w1.place(x=100,y=20,width=400,height=60)

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(t,font=("sans-serif",15,'bold'),values=list_name,textvariable=city_name) 
com.place(x=100,y=110,width=360,height=60)

done_btn=Button(t,text="Done",font=("sans-serif",15,'bold'),bg="#eb9683",fg='white',bd=2,relief=RIDGE,command=get_data)
done_btn.place(x=200,y=200,height=50,width=150)


weather_Climate=Label(t,text="Weather Climate",font=('sans-serif',12,'bold'),fg="white",bg='#5d6396')
weather_Climate.place(x=50,y=280,height=60,width=200)
wl=Label(t,text="",font=('sans-serif',12,'bold'),bg='lightgrey')
wl.place(x=340,y=280,height=60,width=200)

weather_description=Label(t,text="Weather Description",font=('sans-serif',12,'bold'),fg="white",bg='#5d6396')
weather_description.place(x=50,y=360,height=60,width=200)
wd=Label(t,text="",font=('sans-serif',12,'bold'),bg='lightgrey')
wd.place(x=340,y=360,height=60,width=200)

tem=Label(t,text="Temperature",font=('sans-serif',12,'bold'),fg="white",bg='#5d6396')
tem.place(x=50,y=440,height=60,width=200)
temperature=Label(t,text="",font=('sans-serif',12,'bold'),bg='lightgrey')
temperature.place(x=340,y=440,height=60,width=200)


perssure=Label(t,text="Pressure",font=('sans-serif',12,'bold'),fg="white",bg='#5d6396')
perssure.place(x=50,y=520,height=60,width=200)
per=Label(t,text="",font=('sans-serif',12,'bold'),bg='lightgrey')
per.place(x=340,y=520,height=60,width=200)
                      
                      


t.mainloop()

