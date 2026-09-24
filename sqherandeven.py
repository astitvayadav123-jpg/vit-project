numbers=[1,2,3,4,5]
squares=[]
even_number=[]
for number in numbers:
    squares.append(number*number)
    if number%2==0:
        even_number.append(number)
print(squares)
print(even_number)