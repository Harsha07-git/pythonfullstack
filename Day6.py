'''
type conversions
----------------
int-->


an = 78
us = str(an)
om = float(an)
print(om)
print(type(om))
print(type(us))

str-->


an = "90"
Ear = int(an)
print(type(Ear))

an = "Python"
Ear = int(an)
print(type(Ear))   # throws error

an = "90"
Ear = float(an)
print(type(Ear))

an = "90"
Ear = list(an)
print(Ear)
print(type(Ear))
Con = tuple(an)
print(Con)

float-->

car = 990.78
print(int(car))
print(type(str(car)))

List-->

any = [6, 7]
print(str(any))
for j in str(any):
    print(j)

Tuple-->

any = (6, 7)
print(str(any))
for j in str(any):
    print(j)
    
any = {6, 7}
print(type(str(any)))
for j in str(any):
    print(j)

how = (4, 5)
print(list(how))
print(str(how))

int as a user-input
---------------------
num = int(input("Enter a number: "))
print(89+num)

str as a user-input
-------------------
some = input("Write a text: ")

any = input("Enter number: ").split()
print(any)

list as a user_input
--------------------
any = list(map(int, input("Enter numbers: ").split()))
print(any)

tuple as a user_input
----------------------
any = tuple(map(int, input("Enter numbers: ").split()))
print(any)

'''
num = eval(input("Enter: "))
print(type(num))
