Follow the on-screen prompts to interact with the application.

## File Description
- `calorie_tracker.py`: The main Python script that runs the Calorie and Diet Plan Tracker.
- `meals.txt`: A text file used to store meal data persistently.

## Code Explanation
### Import and Global Variables
- **os**: The `os` module is used to interact with the operating system, like checking file existence.
- **FILENAME**: A global constant `"meals.txt"`, which stores the data for all meals.

### Functions
#### `loadMeals(filename)`
- **Purpose**: Load meal data from a specified file.
- **Process**:
  - Initialize an empty list `meals`.
  - Check if the file exists. If it does, open the file and read each line.
  - Split each line into components, create a dictionary for each meal, and append it to the `meals` list.
- **Return**: The list of meals loaded from the file.

#### `saveMeals(meals, filename)`
- **Purpose**: Save the current list of meals to a file.
- **Process**:
  - Open the file in write mode.
  - Iterate over the list of meals, format each meal as a string, and write it to the file.

#### `addMeal(meals)`
- **Purpose**: Add a new meal to the list and update the file.
- **Process**:
  - Prompt the user to enter details for a new meal.
  - Create a dictionary for the new meal and append it to the list.
  - Call `saveMeals` to update the file.
- **User Feedback**: Print a message indicating successful addition.

#### Additional functions (`viewMeals`, `trackDailyIntake`, etc.) describe similarly.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Authors
- **Dhrumit Vekariya** - *Initial work* - [YourGitHubUsername](https://github.com/yourusername)

## Acknowledgments
- Hat tip to anyone whose code was used
- Inspiration
- etc.
