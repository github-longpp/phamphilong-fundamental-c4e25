salary = [
    {
        "name": "Huy",
        "sph": 25,
        "h": 30
    },
    {
        "name": "Quan",
        "sph": 25,
        "h": 20 
    },
    {
        "name": "Duc",
        "sph": 30,
        "h": 40    
    }
]
total = 0
for p in salary:
    slr_1 = p["sph"]*p["h"]
    total += slr_1
    print("Salary of ",p["name"], ":" , slr_1 ,sep=" ")
print("Total of salary : ", total)