print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3) ?")
list_ans = {
    "35" : 1,
    "36" : 2,
    "40" : 3,
    "44" : 4
} 
for k in list_ans:
    print(list_ans[k] , k , sep = ". ")

result = 44
result = str(result)
result_num = list_ans[result]
loop = True
while loop:
    ans = int(input("Enter your answer(1, 2 , 3 , 4): "))
    loop = False
    if ans == result_num:
        print("Bingo")
    else:
        print(":(")
        loop = True

    