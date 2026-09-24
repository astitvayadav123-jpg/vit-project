def search_element(number,key):
    found=False
    for index in range (len(number)):
        if number[index]==key:
            print("ELMENT FOUND AT INDEX :",index)
            found=True
            break
    if found==False:
            print("ELEMENT NOT FOUUND")
number=list(map(int,input("ENTER THE ELEMENTS OF ARRAY SEPERATED BY SPACES:").split()))
key=int(input("ENTER THE ELEMNT YOU WANT TO SEARCH:"))
search_element(number,key)

