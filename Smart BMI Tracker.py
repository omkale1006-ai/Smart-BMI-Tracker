'''
⚖️ Body Mass Index (BMI) Calculator
This program calculates your BMI and tells your weight category.
'''

def body_mass_i(height, weight):
    return round((weight / height**2), 2)

print("👋 Hello! Welcome to the BMI Calculator! ⚖️")

try:
    h = float(input("📏 Enter your height in meters: "))
    w = float(input("⚖️ Enter your weight in kg: "))
    
    bmi = body_mass_i(h, w)
    print(f"🧮 Your BMI is: {bmi}")
    
    if bmi < 18.5:
        print("🟦 You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("✅ Your weight is normal.")
    elif 25 <= bmi < 29.9:
        print("⚠️ You are overweight.")
    else:
        print("❌ You are obese.")
        
    print("🎉 Stay healthy and keep tracking your BMI! 💪")
except ValueError:
    print("❌ Invalid input! Please enter numeric values only.")
