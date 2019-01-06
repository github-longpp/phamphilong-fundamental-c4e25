sh_size = [5, 7 , 300, 90 , 24 , 50 , 75]
print("Hello, my name is Long and there are my sheep sizes")
print(sh_size)

m = max(sh_size)
print("Now my biggest sheep has size" , m , "let's shear it")

n = sh_size.index(m)
sh_size[n] = 8
print("After shearing, here is my flock")
print(sh_size)

for i in range (1,3):
    print("MONTH" , i , ":")
    for j in range (len(sh_size)):
        sh_size[j] += 50
    print("One month has passed, now here is my flock")
    print(sh_size)

    m = max(sh_size)
    print("Now my biggest sheep has size" , m , "let's shear it")

    n = sh_size.index(m)
    sh_size[n] = 8
    print("After shearing, here is my flock")
    print(sh_size)

print("MONTH 3 :")
for j in range (len(sh_size)):
    sh_size[j] += 50
print("One month has passed, now here is my flock")
print(sh_size)

print("My flock has size in total: ", sum(sh_size) )
print("I would get 1010 * 2$ = " , 1010 * 2 , end = "$")