def calculate_factorial(number):
    factorial=1
    for value in range(1,number+1):
      factorial=factorial*value

    return factorial

number=int(input("ENTER THE NUMBER (n) of which u want factorial:"))
if number<0:
   print("FACTORIAL IS DEFINED FOR ONLY POSITIVE NUMBER:")

else:
   result=calculate_factorial(number)
   print("factorialf of ",number,"=",result)