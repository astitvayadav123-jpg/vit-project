numbers=["rama",] #frequency counting and duplicates
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)
unique_numbers=[]
for number in numbers:
   if number not in unique_numbers:
       unique_numbers.append(number)
print(unique_numbers)
