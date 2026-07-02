'''
File Handling
==============
--> File Handler is an object of file to maintain several function of file like creating ,reading,updating and deleting the file

open a file
-----------
1.open()
--> need to use close function to close file

name=open('filename','mode') 
--------------------------------
-----
-----
name.close()


2.with open()
--> need not to use close function

modes
-----
'r'--> is used to reading the file,error if file does not exist.....
'a'--> is used to add the text into the file,if not file does not exist...
'w'--> is used to add the text into file but it will override of all text inside file,if the file does not exist it will create with that name
'x'-->used to create the file...but will through error if we are used
so=open('demo.txt','r')
print(so.read())
so.close()
so=open('demo.txt','a')
print(so.write('sampathirao'))
so.close()
so=open('demo.txt','w')
print(so.write('java'))
so.close()
o/p:
hi kavyasampathirao
11
4

so=open('dm.txt','w')
print(so.write("Kavya"))
so.close()
--> create new file


with open('demo.txt','w') as so:
    print(so.write("kavya"))
o/p: clears before text and add kavya into the file

with open('dem.txt','w') as any:
    any.write('hello')


    
Method
------
write()
read()
------
--> this method can read entire file chunk by chunk where we can specify the side
so=open('demo.txt','r')
print(so.read(10))

readline()
----------
--> can read only one line at a time in a file
so=open('demo.txt','r')
print(so.readline())
so.close()

readlines()
--> read entire file and gives in a list where each line is each index in the list
so=open('demo.txt','r')
print(so.readlines())
so.close()

import os
os.remove('demo.txt')

'''






























