def analyze_array(numbers):
    total=0
    largest=numbers[0]
    smallest=numbers[0]
    for number in numbers:
        total +=number
        if number>largest:
            largest=number
        if number<smallest:
            smallest=number
    average=total/len(numbers)
    return total,average,largest,smallest

numbers=[25,18,42,10,30]
result=analyze_array(numbers)
print(result)