name = input("Enter your Name: ")

s1 = int(input("Enter marks of s1: "))
if s1 < 33:
    print("You have a supplementry in s1")
s2 = int(input("Enter marks of s2: "))
if s2 < 33:
    print("You have a supplementry in s2")
s3 = int(input("Enter marks of s3: "))
if s3 < 33:
    print("You have a supplementry in s3")
s4 = int(input("Enter marks of s4: "))
if s4 < 33:
    print("You have a supplementry in s4")
s5 = int(input("Enter marks of s5: "))
if s5 < 33:
    print("You have a supplementry in s5")  

total = s1 + s2 + s3 + s4 + s5
percentage = total/5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "c"
else:
    grade = "Fail"
    
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage: .2f}")
print(f"Grade: {grade}")
    
    