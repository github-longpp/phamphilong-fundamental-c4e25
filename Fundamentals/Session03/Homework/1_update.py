items = ["T-Shirt" , "Sweater" , "Jeans"]
update = input("Hello manager!!\nDo you want change Sweater to: ")
print("Out items: " , end = " ")
items[1] = update
for i in items:
    print(i , end = "|")
