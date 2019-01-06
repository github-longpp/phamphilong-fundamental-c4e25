#Bài 2.1
sh_size = [5, 7 , 300 , 90 , 24 , 50 , 75]
print("Hello, my name is Long and there are my sheep sizes")
print(sh_size)
#Bài 2.2
m = max(sh_size)
print("Now my biggest sheep has size" , m , "let's shear it")
#Bài 2.3
n = sh_size.index(m)
sh_size[n] = 8
print("After shearing, here is my flock")
print(sh_size)
#Bài 2.4
for i in range (len(sh_size)):
    sh_size[i] += 50
print("One month has passed, now here is my flock")
print(sh_size)
