'''

for i in range(1, 10):
    for j in range(1, 2):
        print(i)
        print(j)
        


num = 9
for j in range(1, 21):
    print(f"{num} x {j} = {j*num}")


so = input("Enter a word: ")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")


num = int(input("Enter a number: "))
armstrong = 0
length = len(str(num))
for i in str(num):
    armstrong += int(i) ** length
if armstrong == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} not an Armstrong number")



num = int(input("Enter the perfect number: "))
perfect_num = 0
for j in range(1, num):
    if num % j == 0:
        perfect_num += j
if perfect_num == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} not a perfect number")



num = int(input("Enter the prime number: "))
count = 0
for k in range(1, num+1):
    if num % k == 0:
        #print(k)
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



star = int(input("Enter the number starts: "))
for g in range(1, star+1):
    for h in range(1, g+1):
        print("*", end="")
    print()



star = int(input("Enter the number starts: "))
for g in range(1, star+1):
    for h in range(1, g+1):
        print(chr(64+h), end="")
    print()



star = int(input("Enter the number starts: "))
count = 0
for g in range(1, star+1):
    for h in range(1, g+1):
        count += 1
        print(count, end=" ")
    print()


star = int(input("Enter the number starts: "))
count = 0
for g in range(star,0,-1):
    for h in range(1, g+1):
        count += 1
        print(count, end=" ")
    print()

star = int(input("Enter the number starts: "))
count = 0
for g in range(star,0,-1):
    for h in range(1, g+1):
        count += 1
        print(chr(64+h), end=" ")
    print()

'''

num = 5
for j in range(1, num+1):
    print(" "*(num-j), end="")
    for i in range(1, j+1):
        print("*", end=" ")
    print()
