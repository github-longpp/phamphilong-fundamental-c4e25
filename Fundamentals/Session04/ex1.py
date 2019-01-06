#Khai báo list -> 1 dãy số ngẫu nhiên.
# -> in ra số nhỏ nhất và vị trí của nó.

#Cách 1:
num = [4 , -79 , 2, 3 , -4 , 5, 6, 7]
# m = min(num)
# print(num.index(m) , m , sep=". ")

# Cách 2:
min = 4
for i in num:
    
    if i < min:
        min = i
print(num.index(min) , min , sep=". ")

