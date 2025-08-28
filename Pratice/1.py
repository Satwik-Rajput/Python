# 1.Print finonacci seris up to n terms
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n =int(input("Enter a number:"))
for i in range(n):
    print(fibonacci(i), end=" ")
print()
print(fibonacci(n))
'''

# 2.Check if anumber is prime using a loop.
'''
def prime(n):
    if n<= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True 
n = int(input("Enter a number:"))
if prime(n):
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")
'''
# Alterbate of 2
'''
def prime():
    n = int(input("Enter a number: "))
    for i in range(2,n):
        if n%i == 0:
            print(f"{n} is not prime number.")
            break
    else:
        print(f"{n} is a prime number.")
prime()
prime()
'''

# 3. Print multiplicaton table of any number.
'''
n = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
'''   

# 4.FInd the factorial of a number using a for loop and while loop.
'''
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
n = int(input("Enter a number:"))
print(f"Factorial of {n} is {factorial(n)}")
'''

# 5.Reverse a number using while loop.
'''
num = int(input("Enter a number:"))
reverse = 0
while num!=0:
    digit = num%10
    reverse = reverse*10+digit
    num = num//10
print(f"Reverse of {num} is {reverse}.")
'''

# 6.{Method 1}: Count the number of digits in a given number.
'''
num = input("Enter a number:")
print(num)
print(len(num))
'''

# 6.{Method 2}.
'''

n = int(input("Enter a number:"))
a = 0
while n!= 0:
    n//=10
    a+=1
print(f"The number of digits is {a}.")
'''

# 7.print all even number between 1 and 100 using loop.
'''
even_number = []
for i in range(101):
    if i%2==0:
        even_number.append(i)
print(even_number)
'''

# 7. Using list comprehension
'''
even_number = [i for i in range(101) if i%2==0]
print(even_number)
'''

# 8. sum of digits in a number.
'''
num = input("Enter a number: ")
total = 0
for digit in num:
    total += int(digit)
print(total)
'''

# 8. Using while loop.
'''
num = int(input("enter a number:"))
total = 0
while num>0:
    digit = num%10
    total+=digit
    num = num//10
print(total)
'''
# print(sum(int(digit)for digit in input("Enter a number:")))


# 9. check if the number is a palindrome.
'''
num = input("Enter a number:")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
'''

# 9. second method useing list method.
'''
n = list(input("Enter a number or a word."))
copy_n = n.copy()
copy_n.reverse()
if copy_n == n:
    print("yes")
else:
    print("No")
'''

# 9. Third method useing while loop.
'''

# 10. Create a pattern of a star or number pyramid triangle inverted triangle
num = int(input("Enter a number:"))
original = num
rev = 0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num//=10
if original == rev:
    print(f"{original} is a ppalindrome.")
else:
    print(f"{original} is not a ppalindrome.")
'''

# 10. Create a pattern of a star or numbers eg(pyramid triangle inverted triangle)
n = int(input("Enter a number:"))
for i in range(n):
    print(" "*(n-i-1)+ "*"*(2*i+1))