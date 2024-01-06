import tkinter
from  tkinter import *
t=tkinter.Tk()
t.config(bg="lightgrey")
t.title("Calculator")
t.geometry('374x330')
calculation=""
def  add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

    
def equal_to():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:   
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
    
    
text_result=Text(t,height=2,width=28,font=("Arial",18))
text_result.grid(columnspan=5)


btn_1=Button(t,text="1",command=lambda:add_to_calculation(1),width=7,font=("Arial",15))
btn_1.grid(row=2,column=1)
btn_2=Button(t,text="2",command=lambda:add_to_calculation(2),width=7,font=("Arial",15))
btn_2.grid(row=2,column=2)
btn_3=Button(t,text="3",command=lambda:add_to_calculation(3),width=7,font=("Arial",15))
btn_3.grid(row=2,column=3)
btn_plus=Button(t,text="+",command=lambda:add_to_calculation("+"),width=7,font=("Arial",15))
btn_plus.grid(row=2,column=4)

btn_4=Button(t,text="4",command=lambda:add_to_calculation(4),width=7,font=("Arial",15))
btn_4.grid(row=3,column=1)
btn_5=Button(t,text="5",command=lambda:add_to_calculation(5),width=7,font=("Arial",15))
btn_5.grid(row=3,column=2)
btn_6=Button(t,text="6",command=lambda:add_to_calculation(6),width=7,font=("Arial",15))
btn_6.grid(row=3,column=3)
btn_sub=Button(t,text="-",command=lambda:add_to_calculation("-"),width=7,font=("Arial",15))
btn_sub.grid(row=3,column=4)

btn_7=Button(t,text="7",command=lambda:add_to_calculation(7),width=7,font=("Arial",15))
btn_7.grid(row=4,column=1)
btn_8=Button(t,text="8",command=lambda:add_to_calculation(8),width=7,font=("Arial",15))
btn_8.grid(row=4,column=2)
btn_9=Button(t,text="9",command=lambda:add_to_calculation(9),width=7,font=("Arial",15))
btn_9.grid(row=4,column=3)
btn_multiply=Button(t,text="*",command=lambda:add_to_calculation("*"),width=7,font=("Arial",15))
btn_multiply.grid(row=4,column=4)


btnopen=Button(t,text="(",command=lambda:add_to_calculation("("),width=7,font=("Arial",15))
btnopen.grid(row=5,column=1)
btn_0=Button(t,text="0",command=lambda:add_to_calculation(0),width=7,font=("Arial",15))
btn_0.grid(row=5,column=2)
btn_close=Button(t,text=")",command=lambda:add_to_calculation(")"),width=7,font=("Arial",15))
btn_close.grid(row=5,column=3)
btn_divide=Button(t,text="/",command=lambda:add_to_calculation("/"),width=7,font=("Arial",15))
btn_divide.grid(row=5,column=4)


btn_clear=Button(t,text="C",command=clear_field,width=7,font=("Arial",15))
btn_clear.grid(row=6,column=1)
btn_equal=Button(t,text="=",command=equal_to,width=7,font=("Arial",15))
btn_equal.grid(row=6,column=3)
t.mainloop()



