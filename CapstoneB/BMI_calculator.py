"""
BMI Calculator - Capstone 3 (Tanish Bhatta)

Requirements: ┌ ┐ └ ┘ ─ │

1) Inputs: height (cm), weight (kg), age, activity level
2) Calculates BMI with category classification
3) Estimates daily calories using Harris-Benedict formula
4) Formatted output with :.2f precision
5) Explicit operator precedence — no shortcuts
"""

print("BMI and Calorie Calculator".center(45, "-"))

name = input("\n1. What is your full name?: ")
weight = float(input("2. Enter your weight (in kg): "))
height = float(input("3. Enter your height (in cm): "))
age = int(input("4. Enter your age: "))
sex = input("5. Enter your sex (m/f): ")
act_fact_multiplier_choose = input("""
6. How much active are you in a week?
                            
1) Sedentary (Little or no exercise)
2) Lightly Active (Light exercise 1–3 days/week)
3) Moderately Active (Moderate exercise 3–5 days/week)
4) Very Active (Hard exercise 6–7 days/week)
5) Extra Active (Very hard daily exercise or physical job)
-> 
""")

if act_fact_multiplier_choose == '1':
    afm = 1.2
elif act_fact_multiplier_choose == '2':
    afm = 1.375
elif act_fact_multiplier_choose == '3':
    afm = 1.55
elif act_fact_multiplier_choose == '4':
    afm = 1.725
elif act_fact_multiplier_choose == '5':
    afm = 1.9
else:
    exit()

word_length = len("Health Analysis Report")
padding = 15
inborder_multiplier = word_length + (2*padding)

bmi = weight/((height/100) ** 2)
if bmi < 18.5:
    bmi_indc = "Underweight"
elif 18.5 <= bmi <= 24.9:
    bmi_indc = "Normal"
elif 24.9 < bmi < 30:
    bmi_indc = "Overweight"
else: 
    bmi_indc = "Obese"

if sex == 'm':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    tdee = bmr * afm
elif sex == 'f':
    bmr =  447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    tdee = bmr * afm
else: exit()

#printout

print(f"""\n
┌{"─" * (inborder_multiplier)}┐
│{"Your Health Profile":^{inborder_multiplier}}│
│{" " * inborder_multiplier}│
│ {f"Name: {name}":<{inborder_multiplier-1}}│
│ {f"Weight: {weight}kg":<{inborder_multiplier-1}}│
│ {f"Height: {height}cm":<{inborder_multiplier-1}}│
│ {f"Age: {age}":<{inborder_multiplier-1}}│
│ {f"Gender: {sex}":<{inborder_multiplier-1}}│
│{" " * inborder_multiplier}│
│{"Health Analysis Report":^{inborder_multiplier}}│
│{" " * inborder_multiplier}│
│ {f"Body Mass Index (BMI): {bmi:.2f} kg/m\u00B2":<{inborder_multiplier-1}}│
│ {f"Weight Classification: {bmi_indc}":<{inborder_multiplier-1}}│
│ {f"Basal Metabolic Rate (BMR): {bmr:.2f} Calories/day":<{inborder_multiplier-1}}│
│ {f"Maintainance Calories (TDEE): {tdee:.2f} Calories/day":<{inborder_multiplier-1}}│
│{" " * inborder_multiplier}│
│{"Goal-Oriented Calorie Targets":^{inborder_multiplier}}│
│{" " * inborder_multiplier}│
│ {f"Weight Loss Target: {tdee-250:.2f} Calories/day":<{inborder_multiplier-1}}│
│ {f"Weight Gain Target: {tdee+250:.2f} Calories/day":<{inborder_multiplier-1}}│
│{" " * inborder_multiplier}│
└{"─" * (inborder_multiplier)}┘
""")

