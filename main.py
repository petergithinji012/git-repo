number=eval(input("Enter the athletes number:"))
if type(number)==int:
   if number==1:
    print("Gold")
   elif number==2:
    print("Silver")
   elif number==3:
    print("Bronze")
   else:
    print("Thanks for participating")
else:
    print("Athletes number should be an integer")


