from person import Person

class Guest(Person):
    
    def __init__(self, name, age, purpose_of_visit):
        super().__init__(name, age)
        self.purpose_of_visit = purpose_of_visit
        
    def enter_details(self):
        super.enter_details()
        self.purpose_of_visit = input("What is the user's purpose of visit: ")
        
    def display_details(self):
        print("\n===========================")
        super().display_details()
        
        print(f"Purpose: {self.purpose_of_visit}")
        print("===========================\n")
        
    def getName(self):
        return super().getName()
        
    def getAge(self):
        return super().getAge()
        
    def getPurposeOfVisit(self):
        return self.purpose_of_visit
    
    def toString(self):
        return f"{super().toString()} '{self.purpose_of_visit}'"
