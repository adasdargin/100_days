# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_90 = 90 * 365
weeks_90 = 90 * 52
month_90 = 90 * 12

days_lived = int(age) * 365
weeks_lived = int(age) * 52
months_lived = int(age) * 12

print(f"You have {days_90 - days_lived} days, {weeks_90 - weeks_lived} weeks, and {month_90 - months_lived} months left.")