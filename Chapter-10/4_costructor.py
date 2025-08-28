class Employee:
    name = "Satwik"   # This is class attribute.
    age = "20"
    role = "AI enginner"
    salary = 1200000

    def __init__(self,name,role,salary):  # This is dunder method and hence it call itself automatically.It starts and ends with __ 
        self.name = name
        self.role = role
        self.salary = salary
        print("Hii how are you?")

Satwik = Employee("Satwik singh Rajput," , "CEO," , 2000000)
print(Satwik.name,Satwik.age , Satwik.role , Satwik.salary)