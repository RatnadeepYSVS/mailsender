from smtplib import *
from getpass import *
obj=SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
email=input('email:')
passcode=getpass('Enter Password: ')#must be your app passcode not your gmail passcode 
obj.login(email,passcode)
fromadd=email
toadd=input('to: ')
subject=input('Subject: ')
mess=input('Mess: ')
msg=f'Subject: {subject}\n\n{mess}'
obj.sendmail(fromadd,toadd,msg)
