marks=list(map(int,input("enter student marks:").split()))
if len(marks)==0:
    print("no marks entered")
else:
    total=0
    pass_count=0
    fail_count=0
    highest=marks[0]
    lowest_mark=marks[0]
for mark in marks:
    total+=mark
    if mark>=40:
        pass_count+=1
    else:
        fail_count+=1
    if mark>highest:
        highest=mark
    if mark<lowest_mark:
        lowest_marks=mark

average=total/len(marks)
print("students:",len(marks))
print("total",total)
print("avegrage=",average)
print("highest=",highest)
print("lowest=",lowest_mark)
print("passed=",pass_count)
print("failed=",fail_count)