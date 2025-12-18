import copy

set1 = {2,-3,0}
set1.add(3)
print(set1)
set1.remove(-3)
print(set1)
print(set1.pop())
print(set1)
student1 = {"maths","english","science"}
student2 = {"maths","history","science"}
print(student1 & student2)
print(student1 | student2)

days = {"monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday"}
weekends = {"monday", "tuesday", "wednesday"}
weekdays = days.difference(weekends)
print(weekdays)

fs1 = frozenset({1,2,3,4,5})
print(fs1)

groceries = {"milk":60,"biskuits":25,"rice":90}
print(groceries)
groceries['milk']=30
print(groceries)



student = {"maths":80.5,"english":84.5,"science":23.5}
l1 = [1,2,3.5,[10,20,30]]
print(l1)
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))
print(f"l1->{l1}",id(l1))
print(f"id(l1)={l1}",id(l1))
print(f"id(l2)={l2}",id(l2))
#for i
for apple in range(1,10):
    print("apple")

#syntax of if
age = float(input("what's your age?"))
if age >= 18:
    print("you are young")
else:
    print("you are child")

num = int(input("enter a number"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# >=90, grade A
marks = float(input("enter your marks"))
if marks >= 90:
    print("your grade is A")
elif marks >= 80 and marks < 90:
    print("your grade is B")
elif marks >= 70 and marks < 80:
    print("your grade is C")
elif marks >= 60 and marks < 70:
    print("you are faild")
