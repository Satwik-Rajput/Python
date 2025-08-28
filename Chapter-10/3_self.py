class Employee:
    name = "Satwik"   # This is class attribute.
    age = "20"
    role = "AI enginner"
    salary = 1200000 

    def getinfo(self):
        print(f"Employee name is: {self.name}")
        print(f"Employee age is: {self.age}")
        print(f"Employee role is: {self.role}")
        print(f"Employee salary is: {self.salary}")

    @staticmethod          # Here @staticmethod is used to make the function independent of the class.
    # def greet(self):     # So,we can use the function without self argument.
    def greet():
        print("Good Morning")
    
Satwik = Employee()

Satwik.greet()
Satwik.getinfo()
# Employee.getinfo(Satwik)