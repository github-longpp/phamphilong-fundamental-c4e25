def get_even_list(l):
    k = []
    for i in l:
        if i % 2 == 0:
            k.append(i)
    return k

a = get_even_list([1,3,5,7,9,10, 11,12,14])
print(a)

even_list = get_even_list([1,2,5,9 ,-10,6])
print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
