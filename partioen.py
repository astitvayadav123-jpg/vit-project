numbers=list(map(int,input("enter array elements by spaces:").split()))         
t=int(input("enter the thersold value:"))
smaller=[]
greaternumber=[]
for number in numbers:
    if number<t:
        smaller.append(number)
    else:
        greaternumber.append(number)
partioned_array=smaller+greaternumber
print("orignal array:",numbers)
print("values smaller than" , t,":",smaller)
print("values greater than or equal to ",t,":",greaternumber)
print("partioned array:",partioned_array)