from person import Person

class Student(Person):

    def __init__(self, name, age, school, studentID, gwa):
        super().__init__(name, age)
        self.school = school
        self.studentID = studentID
        self.gwa = gwa
        
    def enter_details(self):
        super().enter_details()
        self.school = input("Enter school name: ")
        self.studentID = input("What is the student ID: ")
        while int(self.studentID) <= 0:
            print("Error! Invalid Input!")
            self.studentID = input("What is the student ID: ")
        
        self.gwa = input("What is the gwa: ")
        while float(self.gwa) < 0 or float(self.gwa) > 5:
            print("Error! Invalid Input!")
            self.gwa = input("What is the gwa: ")
     
    def display_details(self):
        print("\n===========================")
        super().display_details()
        print(f"School: {self.school}")
        print(f"Student ID: {self.studentID}")
        print(f"GWA: {self.gwa}")
        print("===========================\n")
        
    def getName(self):
        return super().getName()
        
    def getAge(self):
        return super().getAge()
        
    def getSchool(self):
        return self.school
        
    def getStudentID(self):
        return self.studentID
        
    def getGWA(self):
        return self.gwa
        
    def toString(self):
        return f"{super().toString()} {self.school} {self.studentID} {self.gwa}"
            
