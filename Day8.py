'''
elif


stu_name = input("Enter student name: ")
stu_marks = int(input("Enter marks: "))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("Pass")
else:
    print("Failed")



a = input("Enter the numbers: ").split()
num1 = int(a[0])
num2 = int(a[1])
num3 = int(a[2])
if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest number")
else:
    print(f"{num3} is the greatest number")


SBI_bank = {"ATM PIN":"6600"}
pin = input("Enter 4 digit number: ")
if len(pin) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("Invalid pin")
else:
    print("Pls enter 4 digit pin")


for statement
-------------
--> Used to iterate over a sequence
--> beside for the variable is called instance or Loop variable

any = "Python"
an = [1, 2, 3, 4]
so = (5, 6, 7, 8)
for how in any:
    print(how)


range()
-------
range() is in-built function use to generate number in sequence manner

Syntax---> range(start, end, step)

else in for
-----------
--> once the iterations completed this else will be

for i in range(1, 100):
    if i%2 == 0:
        print(i, end="-")
else:
    print("Code ended here")
    

for i in range(50, 100, 3):
    print(i)


break
-----
--> used to exit from the loop based on the condition

continue
--------
--> used to skip the current iteration base on the condition



for i in range(1, 10):
    print(i)
    if i == 5:
        break

for i in range(1, 10):
    if i == 5:
        continue
    print(i)


for i in range(1, 10):
    if i == 3:
        pass        # used to prevent Indentation error
'''
i = 1
while i < 5:
    print(i)
    i += 1
