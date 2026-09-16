#function to calculate sum of number :
def calulate_sum(number):
    number=abs(number)
    total=0
    while number>0:
        digit=number%10
        total=total+digit 
        number=number//10
    return total

number=int(input("ENTER THE INTEGER ,SUM:"))
result=calulate_sum(number)
print("THE SUM OF THE DIGIT OF NUMBER GIVEN:",result)