# Name:           Calorie and Diet Plan Tracker
# Author:         Dhrumit Vekariya
# Date created:   2024-08-02
# Date last:      2024-08-07

# Purpose: This program helps users manage their calorie intake and diet plans.

import os

FILENAME = "meals.txt"

def loadMeals(filename):
    """
    Load meals from a text file.
    """
    meals = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                foodItem, quantity, calories, date = line.strip().split(',')
                meal = {
                    "foodItem": foodItem.capitalize(), 
                    "quantity": float(quantity),
                    "calories": float(calories),
                    "date": date
                }
                meals.append(meal)
    return meals

def saveMeals(meals, filename):
    """
    Save meals to a text file.
    """
    with open(filename, "w") as file:
        for meal in meals:
            line = f"{meal['foodItem']},{meal['quantity']},{meal['calories']},{meal['date']}\n"
            file.write(line)

def addMeal(meals):
    """
    Add a new meal to the meal list and save it.
    """
    foodItem = input("Enter the food item: ").capitalize()
    quantity = float(input("Enter the quantity: "))
    calories = float(input("Enter the calories: "))
    date =  input("Enter the date (YYYY-MM-DD): ")

    meal = {
        "foodItem": foodItem,
        "quantity": quantity,
        "calories": calories,
        "date": date
    }
    meals.append(meal)
    saveMeals(meals, FILENAME)
    print("Meal added successfully!")

def viewMeals(meals):
    """
    View all meals in the meal list.
    """
    for meal in meals:
        print(f"{meal['date']} - {meal['foodItem']} - {meal['quantity']} - {meal['calories']} calories")

def trackDailyIntake(meals):
    """
    Track the total calories consumed on a specific date.
    """
    date = input("Enter the date (YYYY-MM-DD): ")
    dailyGoal = float(input("Enter your daily calorie goal: "))
    totalCalories = sum(meal['calories'] for meal in meals if meal['date'] == date)
    print(f"Total calories consumed on {date}: {totalCalories}")
    if totalCalories <= dailyGoal:
        print("You have reached your daily calorie goal!")
    else:
        print("You have exceeded your daily calorie goal!")

def main():
    """
    Main function to control the flow of the program.
    """
    meals = loadMeals(FILENAME)

    while True: 
        print("\nCalories and Diet Plan Tracker")
        print("1. Add a Meal")
        print("2. View Meals")
        print("3. Track Daily Intake")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addMeal(meals)
        elif choice == "2":
            viewMeals(meals)
        elif choice == "3":
            trackDailyIntake(meals)
        elif choice == "4":
            print("Exiting the program...")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

