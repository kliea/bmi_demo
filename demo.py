# bmi-demo-project
print("BMI DEMO PROJECT")
height = int(input("please input your height in cm: "))
weight = int(input("please input your weight in kg: "))
h = 100
print("\n")
#bmi_calculator
initialheight = height / h
finalheight = round(initialheight ** 2, 2)
bmi = round(weight / finalheight, 1)
print("You're BMI is: " + str(bmi) + " and")

#bmi_categories
if bmi <= 18.5:
    print("You're Underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print("You have normal weight")
elif bmi > 25 and bmi <= 29.9:
    print("You're Overweight")
else:
    print("You have Obesity")

#ending
user_choice = input(" Do you want to play again? (y/n)")
if user_choice in["Y", "Yes","yes"]:
    pass
