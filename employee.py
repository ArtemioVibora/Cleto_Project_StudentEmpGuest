from person import Person

class Employee(Person):
    def __init__(self, name, age, employeeID, job, salary):
        super().__init__(name, age)
        self.employeeID = employeeID
        self.job = job
        self.salary = salary
    
    def enter_details(self):
        super().enter_details()
        self.employeeID = input("What is the user's employee ID: ")
        while int(self.employeeID) <= 0:
            print("Error! Invalid Input!")
            self.employeeID = input("What is the user's employee ID: ")
        self.job = input("What is the user's job: ")
        self.salary = input("What is the user's salary: ")
        while float(self.salary) <= 0:
            print("Error! Invalid Input!")
            self.salary = input("What is the user's salary: ")
            
    def display_details(self):
        print("\n===========================")
        super().display_details()
        
        print(f"Employee ID: {self.employeeID}")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary}")
        print("===========================\n")

    def getName(self):
        return super().getName()
        
    def getAge(self):
        return super().getAge()
        
    def getEmployeeID(self):
        return self.employeeID
        
    def getJob(self):
        return self.job
        
    def getSalary(self):
        return self.salary
        
    def toString(self):
        return f"{super().toString()} {self.employeeID} {self.job} {self.salary}"
        
