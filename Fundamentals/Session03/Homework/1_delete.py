items = ["T-Shirt" , "Skirt" , "Jeans"]
delete = input("Hello manager!!\nDo you want delete: ")
items.remove(delete)
print("Out items:" , end = " ")

for i in items:
    print(i , end = "|")
