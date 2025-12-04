# Daily Calorie Tracker CLI
# Author: Krishan kumar joshi
# Date: 04-12-2025
# Description: Simple CLI tool to log meals and track daily calorie intake.

# Display welcome message
print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals and compare intake to your daily limit.\n")

# Prompt user for number of meals to log
num_meals = int(input("How many meals would you like to log? "))

meals = []
calories = []

# Collect meal names and calorie values
for i in range(num_meals):
    meal_name = input(f"Enter name of meal {i+1}: ")
    meal_cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(meal_cal)

# Ask for daily calorie limit and calculate totals/average
daily_limit = float(input("Enter your daily calorie limit: "))
total_calories = sum(calories)
average_calories = total_calories / num_meals if num_meals else 0

# Display total and average
print(f"\nTotal calorie intake: {total_calories}")
print(f"Average calories per meal: {average_calories:.2f}")

# Compare with daily limit and display message
if total_calories > daily_limit:
    print("Warning: You have exceeded your daily calorie limit!")
else:
    print("Great! You're within your daily calorie limit.")

# Print summary table of meals and calories
print("\nMeal Name\tCalories")
print("-------------------------")
for name, cal in zip(meals, calories):
    print(f"{name}\t\t{cal}")
print(f"\nTotal:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

# Bonus: Ask to save session to file
save = input("\nDo you want to save this session to a file? (yes/no): ")
if save.lower() in ['yes', 'y']:
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorie_log.txt", "a") as f:
        f.write(f"Session Date/Time: {timestamp}\n")
        f.write("Meal Name\tCalories\n")
        f.write("-------------------------\n")
        for name, cal in zip(meals, calories):
            f.write(f"{name}\t{cal}\n")
        f.write(f"Total:\t{total_calories}\n")
        f.write(f"Average:\t{average_calories:.2f}\n")
        if total_calories > daily_limit:
            f.write("Status: Exceeded daily limit\n")
        else:
            f.write("Status: Within daily limit\n")
        f.write("\n")
    print("Session saved to calorie_log.txt")



