n=int(input("Enter your percentage :"))

if n>=80:
    print("Grade A")
elif n>=60 and n<80:
    print("Grade B")
elif n>=40 and n<60:
    print("Grade C")
else:
    print("Failed")