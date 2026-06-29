#name
name=input("What is your name? ")
print(f" my name is  {name}")

#subjects studied
subjects=int(input("Subjects studied are "))

#marks 
marks = []

for i in range(subjects):
    mark=int(input(f"enter marks{i+1}: "))
    marks.append(mark)

print(marks)

#highest marks among every subject
highest=marks[0]
for mark in marks:
    if mark >highest:
        highest=mark
        
print("highest"  if mark>highest highest==mark "{mark}" )


#lowest marks among the list
lowest=marks[0]
for mark in marks:
    if mark<lowest:
        lowest=mark


print(f"lowest marks obtained is : {lowest}")

total=0

#total marks
for mark in marks:
    total += mark
   

print(f"total marks obtained are {total}")

percentage=(total/(subjects*100))*100

print(f"percentage obtained is  {percentage:.2f}")

if percentage >= 90:
    print(f"A")
elif percentage >= 80:
    print(f"B")
elif percentage >= 70:
    print(f"C")
elif percentage >= 60:
    print(f"D")
elif percentage >= 50:
    print(f"E")
else:
    print(f"fail")

if percentage < 40:
    marks_shortage=40-percentage
    print(f"passing marks is 40 . you need {marks_shortage:.2f} more to pass")