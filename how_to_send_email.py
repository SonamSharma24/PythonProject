# how to send mail 
import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)

ob.ehlo()
ob.starttls()
ob.login("sonam247sharma@gmail.com","eate mtph qyxj fcne")

subject="test python"
body=""" I learn Python
 Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
Python is an interpreted and a high-level programming language.
"""
Message="subject:{} \n\n{}".format(subject, body)

listadd=["anjali1184sharma@gmail.com"]
ob.sendmail("sonam247sharma@gmail.com",listadd,Message)
print('send mail')
ob.quit()