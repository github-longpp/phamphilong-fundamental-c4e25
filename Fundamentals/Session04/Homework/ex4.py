#Question 1
print("Ques 1: Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3) ?")
print("1. 35\n2. 36\n3. 40\n4. 44")

result = 4
score = 0
ans = int(input("Enter your answer(1, 2 , 3 , 4): "))
if ans == result:
    print("Bingo")
    score += 1
else:
    print(":(")
#Question 2
print("Ques 2: Estimate this answer (exact calculation not needed)")
print("Jack scored these mark in 5 math tests: 49 , 81 , 72 , 66 , 52. What is mean?")
print("1. About 55\n2. About 65\n3. About 75\n4. About 85")

result = 2
ans = int(input("Enter your answer(1, 2 , 3 , 4): "))
if ans == result:
    print("Bingo")
    score += 1 
else:
    print(":(")

# Question 3
print("Ques 3: Answer the following algebra question")
print("Find x: 10x + 20 = 30")
print("1. x = 1\n2. x = 2\n3. x = 3\n4. x = 4")

result = 1
ans = int(input("Enter your answer(1, 2 , 3 , 4): "))
if ans == result:
    print("Bingo")
    score += 1 
else:
    print(":(")

print("Your score:" , score)