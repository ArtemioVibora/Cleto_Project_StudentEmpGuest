from student import Student as student
from employee import Employee as employee
from guest import Guest as guest
from display_info import Display_Info as display


class App:

    attendance_array = []
    total_number_of_attendees = 0
    
    def enter_person(self):
        flag = True
        user_input = ""
        while flag:
            display.display_options(1)
            user_input = input("What is the user's type: ")
            if user_input == "student":
                s = student("", "", "", "", "")
                s.enter_details()
                print("")
                s.display_details()
                print("\nLoading into array")
                self.attendance_array.append(f"Student: {s.toString()}")
                self.total_number_of_attendees = self.total_number_of_attendees + 1
                
                flag = False
            elif user_input == "employee":
                e = employee("", "", "", "", "")
                e.enter_details()
                e.display_details()
                print("\nLoading into array")
                self.attendance_array.append(f"Employee: {e.toString()}")
                self.total_number_of_attendees = self.total_number_of_attendees + 1
                
                flag = False
            elif user_input == "guest":
                g = guest("", "", "")
                g.enter_details()
                g.display_details()
                print("\nLoading into array")
                self.attendance_array.append(f"Guest: {g.toString()}")
                self.total_number_of_attendees = self.total_number_of_attendees + 1
                
                flag = False
            elif user_input == "cancel":
                flag = False
            else:
                print("Error! Invalid Input")

    def run(self):
        flag = True
        user_input = ""
        while flag:
            display.display_options(0)
            print("")
            user_input = input("What is your input: ")
            if user_input == "exit":
                flag = False
            elif user_input == "enter person":
                self.enter_person()
            elif user_input == "total number":
                print(self.total_number_of_attendees)
            elif user_input == "show attendees":
                print(self.attendance_array)
            else:
                print("Error! Invalid Input!")
                
        
