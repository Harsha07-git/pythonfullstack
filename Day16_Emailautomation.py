'''
SMTP (Simple Mail Transfer Protocol)
------------------------------------
--> This is used to send emails from server to another server

Note:
-----
1.SMTP SSL Port
---------------
465

2. SMTP TLS Port
----------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'

'''

import smtplib
from email.message import EmailMessage
'''
sender = 'harshaguttula07@gmail.com'
password = 'egkxzfpgeeuyckeo'
msg = EmailMessage()

msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'samram5626@gmail.com'

msg.set_content('GOD BLESS YOU SAMUEL ')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)
server.quit()
'''

sender = 'harshaguttula07@gmail.com'
password = 'nvcxtlnlvfmndlgy'
receiver = ['samram5626@gmail.com', 'charansaibera4@gmail.com']
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
for email in receiver:
    msg = EmailMessage()

    msg['Subject'] = 'Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('Hi')

    server.send_message(msg)
    
server.quit()
