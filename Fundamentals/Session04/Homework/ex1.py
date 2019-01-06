inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# Create
inventory["pocket"] = ["seashell" , "strange berry" , "lint"]
print(inventory)

#Delete
inventory["backpack"].remove("dagger")
print(inventory["backpack"])

#Update
inventory["gold"] = 50
print(inventory["gold"])