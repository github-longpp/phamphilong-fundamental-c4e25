# person = ["Quan" , 25 , "Ha Noi" , 3 , False , 125]
# Khó hiểu

person = {
    "name" : "Quan",
    "age"  : 25,
    "location" : "Hanoi",
    "exes" : 3,
    "status" : False,
    "friends" : 125,
}
person["exp"] = 2 #Create
person["name"] = "a.Quan" #Update

if "skills" in person:
    print("Exist")
else:
    print("Not exist")