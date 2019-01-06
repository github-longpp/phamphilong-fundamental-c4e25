items = ["T-Shirt" , "Sweater"]
new = input("Hello manager!!\nEnter new items: ")
print("Out items:" , end = " ")
items.append(new)
for i in items:
    print(i , end = "|")
