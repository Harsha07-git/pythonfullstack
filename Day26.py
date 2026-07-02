'''
Date and time
==============
--> python provides the built-in datetime module to work with date and time

import datetime
--------------
import datetime
today=datetime.date.today()
print(today)
now=datetime.datetime.now()
print(now)
print(f"Year is:{now.year}")
print(f"Month is:{now.month}")
print(f"Date is:{now.date}")
print(f"Day is:{now.day}")
print(f"Hour is:{now.hour}")
print(f"Minutes:{now.minute}")
print(f"Seconds:{now.second}")

Formatting date and time
------------------------
-->strftime() is used to format date and time
%d--> day
%m-->month
%Y-->year
%H-->hour
%M-->minute
%S-->seconds

import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

import datetime
date1=datetime.date(2026,7,2)
date2=datetime.date(2026,6,15)
print(date1-date2)

TIMEDELTA:

import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(future)

___________________________________________________________________
C-TIME:

import datetime
day = datetime.date.today()
print(day.ctime())
__________________________________________________________________
CALENDAR FOR ONE MONTH:

import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

             (or)
             
import calendar
import datetime
today = datetime.date.today()
year = 2027
month = 8
print(calendar.month(year,month))
________________________________________________________
CALENDAR OF AN YEAR:

import calendar
print(calendar.calendar(2027))

___________________________________________________________
PROJECT ON DATETIME THROUGH EMAIL:

import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender = "deepthiseerapu2004@gmail.com"
password = 'zcfrvlwlkygkpvjg'
receiver = "kavs14345@gmail.com"
target_time = '10:20'

msg = EmailMessage()
msg['subject']='greetings'
msg['From']= sender
msg['To']= receiver
msg.set_content('hello hii good morning ')

print(f"Waiting to send email at {target_time}...")
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent at {datetime.now().strftime('%H:%M:%S')}")
        break
    time.sleep(30)
'''










