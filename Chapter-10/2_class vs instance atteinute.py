class Employee:
    name = "Satwik"   # This is class attribute.
    age = "20"
    role = "AI enginner"
    salary = 1200000

Satwik = Employee()
Satwik.name = "Satwik Singh" # Here nmae is instance attribute. 

 # If both class and instance attribute is same then instance attribute will be prefered.

Satwik.role = "Data Scientist" # Here role is instance attribute.

print(Satwik.name) 

print(Satwik.age) 

print(Satwik.role) 

print(Satwik.salary)