loop_count = 0
loop = True
while loop:
    print("Hi")
    print(loop_count)
    loop_count += 1
    if loop_count >= 3:
        loop = False