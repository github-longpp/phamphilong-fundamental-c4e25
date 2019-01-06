loop= True
while loop:
    pw = input("Enter your password again : ")
    loop = False
    if len(pw) < 8:
        loop = True
    if not pw.isalnum():
        loop = True
    if pw.isdigit():
        loop = True
    if pw.isalpha():
        loop = True

print("Your password right!")