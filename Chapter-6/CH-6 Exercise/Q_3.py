T1 = "Make a lot of money"

T2 = "buy now"

T3 ="subscribe this"

T4 = "click this"

Text = input("Enter your message:")

if(T1 in Text or T2 in Text or T3 in Text or T4 in Text):
    print("This message is spam")
else:
    print("This message is not spam")