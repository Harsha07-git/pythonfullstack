Regular Expression
===================
--> RegEx is a sequence of char that form a searching pattern...
--> This can be used to check if a string contain the specified search pattern

-->python has a built-in package called 're' which can be used to work with RegEx...

Functions in re
--------------
1.findall
2.search
3.fullmatch

[]--> a-z,A-Z,0-9 and any specified sequence
. --> here each dot is one char
^ --> this look for the ,string is starting with specified sequence or not
$ --> this look for the string is ending with specified sequence or not
?--> zero or one
*--> zero or more
+ --> one or more
{} -->

Special Sequence
---------------
\S --> no space
\s --> only space
\D--> non-digits
\d --> only -digits
\w --> matches any word char(letters,digits,underscore)
\W --> Non-words


import re
any="RegEx is a sequence of char5 that form7 a searching8 pattern10"
so="seq"
print(re.findall('a',any))
print(re.search('a',any))
print(re.fullmatch(r'[sequence]+',so))
print(re.fullmatch(r'[A-Z a-z]+',any))
print(re.findall('[m-zA-Z]',any))
print(re.findall('[cs]',any))
print(re.search('[cs]',any))
print(re.findall('[5-9]',any))
print(re.findall('sea..',any))
print(re.findall('^RegEx is',any))
print(re.findall('pattern10$',any))
print(re.findall('sea.*n',any))
print(re.findall('sea.+n',any))                                         
print(re.findall('s.{7}',any))
print(re.findall('s.*',any))
print(re.findall('\d',any))
print(re.findall('\D',any))
print(re.findall('\S',any))
print(re.findall('\s',any))
print(re.findall('\w',any))
print(re.findall('\W',any))

mobile=input("Enter 10 digit mobile number:")
how=re.fullmatch('[6-9][0-9]{9}',mobile)
if how:
    print(f"{mobile} is india number")
else:
    print(f"{mobile} is not india number")
















