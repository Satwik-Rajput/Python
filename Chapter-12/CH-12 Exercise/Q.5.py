a = int(input("Enter a number:"))

table = [a*i for i in range(1,11)]

with open("table.txt","a") as f:
    f.write(f"The table of {a}:{str(table)}\n")
