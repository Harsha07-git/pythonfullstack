'''
import re

class Validation:
    def __init__(self):
        self.mobile_pattern = r"^[6-9][0-9]{9}$"
        self.mail_pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
        self.passwords = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*(),.?":{}|<>]).{8,}$'

        
    def mobile(self):
        number = input("1. mobile number: ")
        if re.fullmatch(self.mobile_pattern, number):
            print("Mobile number is VALID")
        else:
            print("Invalid Mobile NUMBER:number Must contain 10 digits starting with 6-9")
            
    def password(self):
        pwd = input("2. password: ")
        if re.fullmatch(self.passwords,pwd):
            print(" Password is VALID")
        else:
            print("INVALID PASSWORD : password must contain atleat one capital letter\n at least small letter\n at least 8 characters\n atleast one special character") 
    
    def mail(self):
        email = input("3. mail: ")
        if re.fullmatch(self.mail_pattern, email):
            print("-> Mail is VALID")
        else:
            print("Invalid Mail: Must end with @gmail.com")

obj = Validation()
obj.mobile()
obj.password()
obj.mail()
'''
