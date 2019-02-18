import mlab
from food import Food

mlab.connect()

# 1. Create
# 1.1 Create a food
# f = Food(title="Banh sai", link="<<link sai>>")
# 1.2 Save it
# f.save()

# # 2. Read
# # 2.1 Get cursor
f_objects = Food.objects()  # Lazy loading # Same a list

# # # 2.2 Process cursor
# f_first = f_objects[0] #Actual data transfering
# print(f_first)

# f = f_objects[1]
# f.update(set__title="Bánh rất rất ngon", set__link="Link ngon")
# f.reload()
# print(f.title)

# f.delete()

f = f_objects.with_id("5c6a6ceede06361f94e906b8")
f.delete()