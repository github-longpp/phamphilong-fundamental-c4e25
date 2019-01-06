# item1 = "Bun dau mam tom"
# item2 = "Pho"
# item3 = "Banh mi sot vang"
# item4 = "Lau"

# items = [] # Empty list
# print(items)
# print(type(items))

# items = ["Bun dau mam tom"]
# print(items)

items = ["Bun dau mam tom", "Pho", "Banh mi", "Lau"]
print(items)
items.append("Banh mi sot vang")  # insert
print(items)

for i in items: #read all
    print(i)

print(items[1]) #readone

items[1] = "Pho xao"
print(items)

items.remove("Pho xao")
print(items)

items.pop(2)
print(items)