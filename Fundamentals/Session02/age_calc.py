yob = int(input("Your age of birth? "))
age = 2018 - yob
print(age)

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")  