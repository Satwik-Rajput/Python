for i in range(50):
    if(i==25):
        break 
    print(i) # break statement stops the loop and the control goes to the next statement after the loop.



for i in range(50):
    if(i==25):
        continue
    print(i) # continue statement skips the current iteration of the loop and the control goes to the next iteration of the loop.



for i in range(5):
    print("ud")
    if i == 2:
     continue  
print(i)
