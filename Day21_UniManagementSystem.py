'''
class Person:
    university_name = "JNTUK"

    def __init__(self, name, age, gender, dept, Ph_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.dept = dept
        self.Ph_no = Ph_no
    def display_info(self):
        print(f"Name : {self.name}\nAge :{self.age}\n{self.gender}")

class Student(Person):
    student_count = 0 
    def __init__(self, name, id_no, age, dept, gender, year, Ph_no):
        super().__init__(name,age,gender,dept,Ph_no)
        self.id_no = id_no
        self.year = year
        Student.student_count += 1 
        
    def display_student(self):
        print(f"Name :{self.name}\n Age :{self.age}\nyear :{self.year}\nGender :{self.gender}")
        
class Facality(Person):
    facality_count = 0
    def __init__(self, name, age, dept, fac_id, gender, Ph_no):
        super().__init__(name, age, gender, dept, Ph_no)
        self.fac_id = fac_id
        Facality.facality_count += 1
    def display_facul0ty(self):
        print(f"Name: {self.name}, Faculty ID: {self.fac_id}, Age: {self.age}, Gender: {self.gender}, Department: {self.dept}, Phone No: {self.Ph_no}")
s1 = Student("Sampath", "501", 20, "CSE", "Male", 3, "76543210")
s2 = Student("Charan", "502", 21, "ECE", "Male", 3, "76543211")
s1.display_student()
s2.display_student()
f1 = Facality("Ramesh", 40, "CSE", "FAC101", "Male", "9876543222")


f1.display_faculty()

print("\nUniversity:", Person.university_name)
print("Total Students:", Student.student_count)



print("=========================**JNTUK**========================")
print()
class Person:
    university_name = "JNTUK"

    def __init__(self, name, age, gender, dept, ph_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.dept = dept
        self.ph_no = ph_no

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Department: {self.dept}, Phone No: {self.ph_no}")

        print()

class Student(Person):
    student_count = 0

    def __init__(self, name, id_no, age, dept, gender, year, ph_no):
        super().__init__(name, age, gender, dept, ph_no)
        self.id_no = id_no
        self.year = year

        Student.student_count += 1

    def display_student(self):
        print()
        print(f"Name: {self.name}\nID No: {self.id_no}\nAge: {self.age}\nYear: {self.year}\nGender: {self.gender}\nDepartment: {self.dept}\nPhone No: {self.ph_no}")


class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, dept, fac_id, gender, ph_no):
        super().__init__(name, age, gender, dept, ph_no)
        self.fac_id = fac_id

        Faculty.faculty_count += 1

    def display_faculty(self):
        
        print(f"Name: {self.name}\nFaculty ID: {self.fac_id}\nAge: {self.age}\nGender: {self.gender}\nDepartment: {self.dept}\nPhone No: {self.ph_no}")



s1 = Student("Sampath", "501", 20, "CSE", "Male", 3, "76543210")
s2 = Student("Charan", "502", 21, "ECE", "Male", 3, "76543211")
print("==========Student Details==========")
s1.display_student()
s2.display_student()


f1 = Faculty("Ramesh", 40, "CSE", "FAC101", "Male", "9876543222")
print("=========Facality Details=========")
f1.display_faculty()


class University:
    university_name = "CODEGNAN UNIVERSITY"

    def display_university(self):
        print(f"University Name : {University.university_name}")


class Person(University):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        self.display_university()
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Gender          : {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, department):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print("\n----- STUDENT DETAILS -----")
        self.display_person()
        print(f"Student ID      : {self.student_id}")
        print(f"Department      : {self.department}")


class Faculty(Person):
    def __init__(self, name, age, gender, faculty_id, subject):
        super().__init__(name, age, gender)
        self.faculty_id = faculty_id
        self.subject = subject

    def display_info(self):
        print("\n----- FACULTY DETAILS -----")
        self.display_person()
        print(f"Faculty ID      : {self.faculty_id}")
        print(f"Subject         : {self.subject}")


class LabAssistant(Person):
    def __init__(self, name, age, gender, employee_id, lab_name):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.lab_name = lab_name

    def display_info(self):
        print("\n----- LAB ASSISTANT DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Lab Name        : {self.lab_name}")


class Librarian(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

    def display_info(self):
        print("\n----- LIBRARIAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")


class Watchman(Person):
    def __init__(self, name, age, gender, employee_id, shift):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.shift = shift

    def display_info(self):
        print("\n----- WATCHMAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Shift           : {self.shift}")


# Objects
s1 = Student("sampath", 21, "Male", "S101", "AI&DS")
f1 = Faculty("raghu", 40, "Male", "F101", "Python")
l1 = LabAssistant("Suresh", 30, "Male", "L101", "Python Lab")
lb1 = Librarian("suneetha", 35, "Female", "LB101")
w1 = Watchman("Ravi", 45, "Male", "W101", "Night")

# Display
s1.display_info()
f1.display_info()
l1.display_info()
lb1.display_info()
w1.display_info()
 
'''
class University:
    university_name = "CODEGNAN UNIVERSITY"

    def display_university(self):
        print(f"University Name : {University.university_name}")


class Person(University):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        self.display_university()
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender:{self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, department):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print("----- STUDENT DETAILS -----")
        self.display_person()
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")


class Faculty(Person):
    def __init__(self, name, age, gender, faculty_id, subject):
        super().__init__(name, age, gender)
        self.faculty_id = faculty_id
        self.subject = subject

    def display_info(self):
        print("----- FACULTY DETAILS -----")
        self.display_person()
        print(f"Faculty ID: {self.faculty_id}")
        print(f"Subject : {self.subject}")


class LabAssistant(Person):
    def __init__(self, name, age, gender, employee_id, lab_name):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.lab_name = lab_name

    def display_info(self):
        print("----- LAB ASSISTANT DETAILS -----")
        self.display_person()
        print(f"Employee ID: {self.employee_id}")
        print(f"Lab Name: {self.lab_name}")


class Librarian(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

    def display_info(self):
        print("\n----- LIBRARIAN DETAILS -----")
        self.display_person()
        print(f"Employee ID : {self.employee_id}")


class Watchman(Person):
    def __init__(self, name, age, gender, employee_id, shift):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.shift = shift

    def display_info(self):
        print("\n----- WATCHMAN DETAILS -----")
        self.display_person()
        print(f"Employee ID : {self.employee_id}")
        print(f"Shift: {self.shift}")


class Cleaner(Person):
    def __init__(self, name, age, gender, employee_id, area):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.area = area

    def display_info(self):
        print("\n----- CLEANER DETAILS -----")
        self.display_person()
        print(f"Employee ID : {self.employee_id}")
        print(f"Cleaning Area: {self.area}")


class Canteen(University):
    def __init__(self, canteen_name, location, manager):
        self.canteen_name = canteen_name
        self.location = location
        self.manager = manager
        print("\n----- CANTEEN DETAILS -----")

    def display_info(self):
        
        print("\n----- CANTEEN DETAILS -----")
        print(f"Canteen Name: {self.canteen_name}")
        print(f"Location: {self.location}")
        print(f"Manager : {self.manager}")





 

s1 = Student("Sampath", 22, "Male", "S101", "CSE")
f1 = Faculty("Bushan", 40, "Male", "F101", "Python")
la1 = LabAssistant("Nikhil", 30, "Male", "L101", "Python Lab")
lb1 = Librarian("Mohi", 35, "Female", "LB101")
w1 = Watchman("Charan", 45, "Male", "W101", "Night")
cl1 = Cleaner("Raju", 42, "Male", "CL101", "Block A")

c1 = Canteen("Main Canteen", "Block A", "Sita")






s1.display_info()
f1.display_info()
la1.display_info()
lb1.display_info()
w1.display_info()
cl1.display_info()

c1.display_info()

