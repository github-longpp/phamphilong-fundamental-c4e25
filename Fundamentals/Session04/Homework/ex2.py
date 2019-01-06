prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# Read fruit.
for k in prices.keys():
    print(k)
    print("price:", prices[k])
    print("stock:", stock[k])

# Calculate money.
money = 0
for i in prices.keys():
    one = prices[i] * stock[i]
    money += one

print("Total money you would make:" , money)