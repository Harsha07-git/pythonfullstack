'''
Built-in functions
------------------
print()
input()
len()
type()
max()
min()


m = [3, 4, 1, 2]
print(sorted(m))    # sorted for just that statement
print(m)

m.sort()    # sort sorts the list permenantly
print(m)

Recursive functions
-------------------
--> A Recursive function that calls itself to solve a problem by breaking into small or
simple sub-problems


def fac(num):
    if num == 1:
        return 1
    return num*fac(num-1)
print(fac(5))


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a+b
        a = b
        b = c

fibonacci(int(input("Enter the number: ")))


def even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
even(7)


def prime_number(num):
    count = 0
    for k in range(1, num+1):
        if num % k == 0:
            #print(k)
            count += 1
    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

prime_number(7)

return
------
this ends a function execution and sends a value back to the code that called the function

def add(a, b):
    return a+b
res = add(4, 5)
print(res)

Lambda functions
---------------
--> A Lambda function is a small anonymous function
lambda can take n number of arguments, but only one expression

syntax--> lambda arguments : expression
'''
so = lambda a,b,c: a+b+c
print(so(3, 4, 9))
