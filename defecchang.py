def exchnage_value(a,b):
    temporary=a
    a=b
    b=temporary
    return a,b

x=int(input("ENTER THE NUMBER X:")) 
y=int(input("ENTER THE  NUMBER Y:"))
print("BEFORE EXCHANGE")
print("x=",x)
print("y=",y)
x,y=exchnage_value(x,y)
print("AFTER EXCHAMGE")
print("x=",x)
print("y=",y)
