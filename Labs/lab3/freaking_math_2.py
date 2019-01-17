from random import choice
ques = ["1 + 2 = 3", "3 + 4 = 5" , "5 + 6 = 10"]
while True:
    que = choice(ques)
    print(que)
    ans = input("Answer (y/n)")
    if que == "1 + 2 = 3":
        result = "y"
    if que == "3 + 4 = 5":
        result = "n"
    if que == "5 + 6 = 10":
        result = "n"
    if ans == result:
        print("Yay")
    else:
        print("Nay")
