#This code uses your weight and height to calculate body mass index (BMI)
#Formula for BMI = weight divide by height^2.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_an_int = int(bmi)
print(bmi_an_int)