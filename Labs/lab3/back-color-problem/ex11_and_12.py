def is_inside(point, rect):
    # rect= [x1 ,x2 ,y1 ,y2] , point[x ,y]
    print(point , " inside" , rect)
    if (rect[0] <= point[0] <= rect[1] and rect[2] <= point[1] <= rect[3]):
        result = True
    else:
        result = False
    return result


# a = is_inside([8 ,5], [4,8,4,8])
# print(a)
# # Test function
# test_point = is_inside([5 ,5] , [4,8,4,8])
# if test_point == True:
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")
