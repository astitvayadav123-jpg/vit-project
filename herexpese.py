total_sales=0
while True:
    sales=float(input("ENTER SALES VALUE:"))

    if sales==0:
        break
    total_sales+=sales

print("TOTAL SALES=",total_sales)