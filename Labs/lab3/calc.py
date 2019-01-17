# x = int(input("nhập x :"))
# y = int(input("nhập y :"))
# op = input("Nhập phép tính: ")
#     # if phep_tinh == "+":
#     #     result = x + y
#     # elif phep_tinh == "-":
#     #     result = x - y
#     # elif phep_tinh == "x":
#     #     result = x * y
#     # elif phep_tinh == "/":
#     #   
#     #     result = x / y
#     # 
#     # elif phep_tinh == "%":
#     #     result = x % y

# print(x , phep_tinh , y , "=" , result)

def eval(x, y ,op):
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "%":
        result = x % y
    return result

# r = eval(x , y , op)
# print(r)


# def sayHi(n):
#     print("Hi")
#     print("Hi" , n)
#     print("Bye Bye")

# def add(a, b):
#     r = a + b
#     return r:
    
# s = add(4,5)
# print(s)

# t = add(8,9)
# print(t)