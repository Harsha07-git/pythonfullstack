'''
Error Handling
==============
try block
---------
--> the try block,test a block of code for error

Except block
-------------
-->The except block let handle if the code cntain errors...

else block
-----------
This  will be exicuted, if the try block has no error in the code

finally  block
--------------
This will executed either try block contain error or not...


try:
    print(a)
except:
    print("it an error")
else:
    print("There is no error")
finally:
    print("The End")


try:
    print(10/0)
except:
    print("This will handle ZeroDivisionError")


try:
    print(a)
except:
    print("This will handle NameError")
else:
    print("No Error")
    

try:
    print(a)
    print(5+"Py")
except TypeError:
    print("This will handle TypeError")
except NameError:
    print("This will handle NameError")
else:
    print("No error")

'''

try:
    print(a)
except:
    print("Error")
else:
    print("No Error")
finally:
    print("The End")
    
    
    
   
