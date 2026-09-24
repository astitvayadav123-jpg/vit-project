print("""QUESTION 1:Which of the following is used to define a block of code in Python?
a) Curly braces
b) Parentheses
c) Indentation
d) Quotation marks""")
answer=str(input("ENTER YOUR ANSWER FROM a,b,c,d:"))
if answer=="c":
    print("YOUR ANSWER IS CORRECT,PLEASE DON'T ANSWER IN CAPTIAL LETTER")
if answer=="b"or answer=="a"or answer=="d":
    print("YOUR ANSWER IS INCORRECT, CORRECT ANSWER IS  OPTION (c)")
else:
    print("PLEASE ENTER A VALID CHOICE,ANSWER AGAIN ")
    answer=str(input("ENTER YOUR ANSWER FROM a,b,c,d:"))

    