**Import and Global Variables**
**os: ** The **os** module is used to interact with the operating system, like checking file existence.
**FILENAME:** A global constant set to **"meals.txt"**, which stores the data for all meals.
**Functions**
**loadMeals(filename)**

**Purpose:** Load meal data from a specified file.
**Process:**
Initialize an empty list **meals.**
Check if the specified file exists. If it does, open the file and read each line.
Split each line into components **(foodItem, quantity, calories, date)**, create a dictionary for each meal, and append it to the **meals** list.
**Return:** The list of meals loaded from the file.
**saveMeals(meals, filename)**

**Purpose:** Save the current list of meals to a file.
**Process:**
Open the specified file in write mode.
Iterate over the list of meals, format each meal as a string, and write it to the file.
**addMeal(meals)**

**Purpose:** Add a new meal to the list and update the file.
**Process:**
Prompt the user to enter details for a new meal (food item, quantity, calories, date).
Create a dictionary for the new meal and append it to the list of meals.
Call saveMeals to update the file with the new meal.
**User Feedback:** Print a message indicating successful addition.
**viewMeals(meals)**

**Purpose:** Display all recorded meals.
**Process:** Iterate over the list of meals and print each one.
trackDailyIntake(meals)

**Purpose:** Calculate and display the total calorie intake for a specific date compared to a user-defined goal.
**Process:**
Prompt the user for a date and a daily calorie goal.
Compute the total calories consumed on that date.
Compare the total calories with the goal and provide feedback whether the user met or exceeded the goal.
