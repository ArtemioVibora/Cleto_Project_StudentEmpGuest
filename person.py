class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def enter_details(self):
        self.name = input("What is the user's name: ")
        self.age = input("How old is the user: ")
        while int(self.age) <= 10:
            print("Error: Invalid Input!")
            self.age = input("How old is the user: ")
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
        
    def toString(self):
        return f"{self.name} {self.age}"
