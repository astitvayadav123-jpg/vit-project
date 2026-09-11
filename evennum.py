def count_evennums(numbers):
    count=0
    for number in numbers:
        if number%2==0:
            count=count+1
    return count 


def count_oddnums(numbers):
    count=0
    for number in numbers:
        if number%2!=0:
            count=count+1
    return count
        

numbers=list(map(int,input("ENTER THE ELEMENT SEPRATED BY SPCES:").split()))
even=count_evennums(numbers) 
print("NUMBER OF EVEN NUMBER ARE:",even)
odd=count_oddnums(numbers)
print("NUMBER OF ODD NUMBER ARE:",odd)