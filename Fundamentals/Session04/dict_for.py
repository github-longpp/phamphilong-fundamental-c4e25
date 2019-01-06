person = {
    "name" : "Quan",
    "age"  : 25,
    "location" : "Hanoi",
    "exes" : 3,
    "status" : False,
    "friends" : 125,
}
# Debug

# for k in person.keys():
#     print(k)

# for v in person.values():
#     print(v)

for k,v in person.items():
    print(k , v , sep=": ")