# Base Class: Employee
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
  # Method to return employee details
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: INR{self.salary:,.2f}"
    
  # Method to raise salary
    def raise_salary(self,percentage):
        increase = self.salary * (percentage / 100)
        self.salary += increase
        print(f"{self.name}'s new salary after {percentage}% raise: INR {self.salary:,.2f}")
 
# Subclass: Manager     
  
class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
        
# Override get_details()   
     
    def get_details(self):
        return (f"Manager Name: {self.name}, Age: {self.age}," 
        f"Salary: INR{self.salary:,.2f}, Team size: {self.team_size}"
        )
        
        # Raise salary method    
        
    def raise_salary(self,percentage):
        super().raise_salary(percentage)
        
# Subclass: Designer

class Designer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
        
  # Override get_details()
    def get_details(self):
         return (f"Deginer Name: {self.name}, Age: {self.age}," 
        f"Salary: INR{self.salary:,.2f}, "
        f"Programmig Language: {self.programming_language}"
        )
         
 # Raise salary method
    def raise_salary(self, percentage):
        super().raise_salary(percentage)
        
# Step 1: Create objects
manager1 = Manager("Alice", 30, 150000, 10)
designer1 = Designer("Bob", 35, 79000, "Python")

print("\n--------------Initls Details------------")
print(manager1.get_details())
print(designer1.get_details())

# Step 2: Apply salary raise
print("\n---------------salary Raise---------------")
manager1.raise_salary(10)     # 10% increase
designer1.raise_salary(15)     #%15% increase

# Step 3: Display updated details
print("\n----------Display updated Details--------")
print(manager1.get_details())
print(designer1.get_details())
print("\n")

        