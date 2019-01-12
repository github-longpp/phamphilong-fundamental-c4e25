from matplotlib import pyplot

# 1. Prepare data
machine_count = [18 , 4 , 2]
# 2. Prepare labels
machine_name = ["PC" , "MAC" , "Linux"]
# 3. Draw pie
pyplot.pie(machine_count , labels=machine_name , autopct="%.1f%%" , shadow=True , explode=[0,0.1 ,0])
pyplot.title("PC, MAC and LINUX")
pyplot.axis("equal")
# 4. Show
pyplot.show()