'''
# fibonacci

num = 0
num2 = 1

def fibonacci(num, num2):
    limit = int(input("Enter the limit: "))
    print(num, num2, end=" ")
    for i in range(1, limit):
        num3 = num + num2
        num = num2
        num2 = num3
        print(num3, end=" ")
        
fibonacci(num, num2)

'''
lst = [2, 5, 7, 9, 2, 7]
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates(lst))

# count the words in the string
so = "Quantum computing is an advanced field of technology that harnesses the laws of quantum mechanics"
count = 0

def word_str(so, count):
    for i in so:
        count += 1
    print(count)
    
word_str(so, count)

