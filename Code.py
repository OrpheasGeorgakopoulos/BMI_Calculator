weight = float(input("Enter Weight (KG): "))
height = float(input("Enter Height (M): "))

print("-------------")

bmi = weight /(height * height)

print("BMI: ", bmi)

if bmi <18.5:
    print("You are underweight!")
elif bmi <25:
    print("You are normal!")
elif  bmi<30:
    print("You are overweight!")
else:
    print("You are obese!")
