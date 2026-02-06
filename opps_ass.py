class Employee:
    def __init__(self):
        self.EmployeeID = 0
        self.Gender = ""
        self.Salary = 0
        self.PerformanceRating = 0

    def get(self):
        print("\n--- Enter Employee Details ---")
        try:
            self.EmployeeID = int(input("Enter Employee ID: "))
            self.Gender = input("Enter Gender: ")
            self.Salary = int(input("Enter Salary: "))
            
            while True:
                rating = int(input("Enter Performance Rating (1-5): "))
                if 1 <= rating <= 5:
                    self.PerformanceRating = rating
                    break
                else:
                    print("Invalid input. Rating must be between 1 and 5.")
                    
        except ValueError:
            print("Invalid input. Please enter numbers for ID, Salary, and Rating.")
            self.EmployeeID = 0
            self.Salary = 0
            self.PerformanceRating = 0


class Department:
    def __init__(self):
        self.DepartmentName = ""

    def get_department(self):
        print("\n--- Enter Department Details ---")
        self.DepartmentName = input("Enter Department Name: ")


class Manager(Employee, Department):
    def __init__(self):
        Employee.__init__(self)
        Department.__init__(self)
        print("\n(New Manager object created)")

    def display_all_details(self):
        print("\n" + "="*30)
        print("    MANAGER FULL PROFILE")
        print("="*30)
        
        print(f"Employee ID: \t{self.EmployeeID}")
        print(f"Gender: \t{self.Gender}")
        print(f"Salary: \t${self.Salary:,}")
        print(f"Rating: \t{self.PerformanceRating}/5")
        
        print("-"*30)
        
        print(f"Department: \t{self.DepartmentName}")
        print("="*30)


if __name__ == "__main__":
    
    print("Creating a new Manager profile...")
    
    mgr1 = Manager()
    
    mgr1.get()
    
    mgr1.get_department()
    
    mgr1.display_all_details()

