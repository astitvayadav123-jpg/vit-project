def has_passed(marks1,marks2,marks3):
    passed=marks1>=40 and marks2>=40 and marks3>=40
    return passed
marks1=float(input("ENTER THE MARKS IN SUBJECT 1:"))
marks2=float(input('ENTER THE MARKS IN SUBJECT 2:'))
marks3=float(input('ENTER THE MARKS IN SUBJECT 3:'))
valid_marks=(
    0<=marks1<=100
    and 0<=marks2<=100
    and 0<=marks3<=100
)
if not valid_marks:
    print("INVALID MARKS! ENTER MARKS BETWEEN 0 AND 100.")
else:
    result=has_passed(marks1,marks2,marks3)
    print("PASSED ALL SUBJECT",result)
if result:
    print("result:pass")
else:
    print("result:fail")
