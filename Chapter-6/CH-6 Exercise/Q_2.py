m1 = int(input("Enter your subject 1st marks:"))
m2 = int(input("Enter your subject 2nd marks:"))
m3 = int(input("Enter your subject 3rd marks:"))

total_percentge =((((m1+m2+m3)*100)/300))  

if(total_percentge>40 and m1>=33 and m2>=33 and m3>=33):
    print("Yor are passed and your percentage is",total_percentge)
else:
    print("You are failed,better tyr next time by the way your precentage is",total_percentge)

if(m1<33):
    print("Try to improve your 1st subject")
elif(m2<33):
    print("Try to improve your 2nd subject")
elif(m3<33):
    print("Try to improve your 3rd subject")