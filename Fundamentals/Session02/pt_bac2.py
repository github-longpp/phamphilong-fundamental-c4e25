a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
a_2 = a * 2
if a == 0:
    print("Phuong trinh co 1 nghiem la x = " , -c/b )
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x1 = ((-b) / a_2)
        print("Phuong trinh co nghiem duy nhat la x = " , x1)
    else:
        delta_sqrt = delta ** 0.5
        x2 = ((-b + delta_sqrt)  / a_2)
        x3 = ((-b - delta_sqrt) / a_2)
        print("Phuong trinh co 2 nghiem la x1 = " , x2 , "x2 = " , x3)
