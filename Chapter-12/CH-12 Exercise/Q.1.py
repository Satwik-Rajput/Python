try:
    with open('1.txt') as f1:
        print(f1.read())
except Exception as e:
        print(e)

try:
    with open('2.txt') as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open('3.txt') as f3:
        print(f3.read()) 
except Exception as e:
    print(e)  

print('This programm does not crash.')