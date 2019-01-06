eng_dict = {
    "mom" : "Mẹ",
    "dad" : "Bố",
    "son" : "Con trai",
    "daughter" : "Con gái",
    "sun" : "Mặt trời",
    "white" : "Màu trắng",
    "red" : "Màu đỏ",
    "blue" : "Xanh dương",
    "green" : "Xanh lá cây",
}
while True:
    a = input("Enter you word: ")

    if a in eng_dict:
        print(eng_dict[a])
    else:
        print("This word is'n exist")
        ques = input("Do you want to add dict (y/n) : ")
        if ques == "y":
            trans_new = input("Enter translation: ")
            eng_dict[a] = trans_new

# b = input("Do you want to update dict (y/n) : ")
# if b == "y":
#     c = input("What word you want update : ")
#     eng_dict[a] = c

# print(a , " is " , eng_dict[a])


