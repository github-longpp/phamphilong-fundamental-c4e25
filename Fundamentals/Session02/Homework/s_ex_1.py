h = int(input("Enter your height: "))
w = int(input("Enter your weight: "))
h /= 100
bmi = w / (h * h)
print("Your BMI: " , bmi)
if(bmi < 16):
    print("Severely underweight")
elif(bmi < 18.5):
    print("Underweightn")
elif(bmi < 25):
    print("Normal")
elif(bmi < 30):
    print("Overweight")
else:
    print("Obese")
