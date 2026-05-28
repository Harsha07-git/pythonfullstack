'''
List Comprehension
------------------
-->LC offers a shortest syntax when we want to create a new list from existing list

syntax --> variable_name = [expression loop condition]

old_ = list(map(int, input().split()))
new_ = [so if so % 2 != 0 else "even" for so in old_]
print(new_)

Generators
----------
--> Generators in python are special type of iterable, allowing users to iterate over
data efficiently without storing everything in memory...
--> They generate the values lazily using yield keyword

Why to use gen
--------------
-->Generators do not store the entire data set in memory, they generate values on the
fly or runtime.
--> Avoiding the unnecessary storage of data speed up execution.

--> These are used to read the data chunk ny chunk

How it works
------------
--> It looks like normal function but uses the yield keyword instead of return
--> when the function is called, it does not execute immediately. Instead, it return a
generator object which can be iterated using loop or the next() function  

def simple_gen():
    print("Start")
    yield 1
    print("Start")
    yield 2
    yield 3
    #print("end")
gen = simple_gen()
print(next(gen))
print(next(gen)

print(next(gen))


def sqr(num):
    result = []
    for i in range(1, num+1):
        result.append(i*i)
    return result
print(sqr(5))

def any(num):
    for i in range(1, num+1):
        yield i*i
a = any(10)
for i in range(10):
    print(next(a))

def fibonacci(num):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(num):
        c = a + b
        a = b
        b = c
        print(c, end=" ")
fibonacci(5)
'''

so = 'Quantum computing is an advanced field of technology that harness the law'
any = ""
for j in so:
    if j not in "AEIOUaeiou":
        any += j

print(any)
