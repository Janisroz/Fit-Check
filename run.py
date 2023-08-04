import json


def welcome():
    """
    Welcomes user to program
    """
    print("Welcome to Fit Check!")
    print("We will ask you some questions,")
    print("do some calculations and then give some recommendations")
    print("But first...\n")


def get_name():
    """
    Validates user input as only letters and less than 20 characters
    """

    try:
        name = input("Please Enter your first name:\n")
        if str.isalpha(name) and len(name) < 20:
            return name
        else:
            raise ValueError(
                f"Name must only be letters and less than 20 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        get_name()

    return True


def bmi(name):
    """
    Calculates user BMI by getting height and weight and validates both
    """
    print(f"\nWelcome {name}\n")
    print("----------------------------------------------------")
    print("Firstly we will calculate your Body Mass Index (BMI)")
    print("This figure is used to estimate your total amount of body fat.")
    print("It is only an approximate measure of the")
    print("best weight for your health.")
    print("----------------------------------------------------\n")

    # get height & validate
    height = get_height()

    # get weight & validate
    weight = get_weight()

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # give results
    result = bmi_result(bmi, name)

    return result


def get_height():
    """
    Gets user weight input and validates
    """
    try:
        height = int(input("Enter your height e.g.180 (Do not include cm):\n"))
        if height < 300:
            return height
        else:
            raise Exception
    except Exception:
        print("Height must be numbers only and less than 300")
        get_height()


def get_weight():
    """
    Gets user weight input and validates
    """
    try:
        weight = int(input("Enter your weight e.g.80 (Do not include kg):\n"))
        if weight < 300:
            return weight
        else:
            raise Exception
    except Exception:
        print("Weight must be numbers only and less than 300")
        get_weight()


def calculate_bmi(h, w):
    """
    Calculates BMI & rounds to 2 decimal places
    """
    h_in_m = h / 100
    bmi = w / (h_in_m**2)
    bmi = round(bmi, 2)
    return bmi


def bmi_result(bmi, name):
    """
    Gives user info and recommendations depending on their BMI
    """
    result = ""
    if bmi < 18.5:
        result = "underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        result = "healthy weight"
    elif bmi >= 24.9 and bmi < 29.9:
        result = "overweight"
    elif bmi >= 30:
        result = "obese"
    else:
        print("Error with bmi please try again")
        main()

    recommendation = ""
    if result == "underweight":
        recommendation = "weight gain"
    elif result == "healthy weight":
        recommendation = "maintenance"
    elif result == "overweight" or result == "obese":
        recommendation = "weight loss"
    else:
        print("Error with result please try again")
        main()
    print("\n----------------------------------------------------")
    print(f"{name}, your BMI is {bmi}")
    print("----------------------------------------------------\n")
    print("----------------------------------------------------")
    print(f"This result classifies you as {result}")
    print("With this result we recommend that")
    print(f"your focus is on {recommendation}")
    print("----------------------------------------------------\n")

    return recommendation


def recc_calories(name, recommendation):
    """
    Collect info to give user a recommendation on daily calorie consumption
    """
    print("----------------------------------------------------")
    print("Next we will calculate your recommended calories")
    print("We will do this by getting your gender, age and activity level")
    print("and creating a recommendation based on this")
    print("----------------------------------------------------\n")
    # get gender & validate
    gender = get_gender()

    # get age & validate
    age = get_age()
    # get activity level and validate
    print("\n----------------------------------------------------")
    print("Activity level is your total amount of daily physical activity")
    print("It is split into three levels:")
    print("Sedentary is inactive where your only activity is daily life\n")
    print("Moderately active is at least 60 mins 3 days a week")
    print("of moderately intense excercise for  per week\n")
    print("Active is at least 60 mins 5 days a week")
    print("of moderately intense to intense exercise per week")
    print("----------------------------------------------------\n")
    activity_level = get_activity_level()
    recc_calories = get_recc_calories(gender, age, activity_level)

    # Give recc calories
    print("\n----------------------------------------------------")
    print(f"{name} your daily recommended calories for your age")
    print(f"and acitivity level is {recc_calories} calories")
    print("per day")
    print("By maintaining this amount of calories you will be")
    print(f"on track to reaching our recommendation of {recommendation}")
    print("----------------------------------------------------\n")


def get_gender():
    """
    Get gender of user
    """
    try:
        print("----------------------------------------------------")
        print("Please tell us your gender\nm - male\nf - female")

        gender = input("Input your gender:\n")
        if gender == "m" or gender == "f":
            return gender
        else:
            raise ValueError(
                "Please choose m for male or f for female"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        get_gender()


def get_age():
    """
    Get age of user
    """
    try:
        age = int(input("\nPlease tell us your age from 18-100:\n"))
        print("----------------------------------------------------\n")
        if age >= 18 and age <= 100:
            return age
        if age < 18 or age > 100:
            raise ValueError

    except ValueError:
        print("Age must be greater than 18 and less than 100\n")
        get_age()


def get_activity_level():
    """
    Get activity level of user
    """
    try:
        print("Choose your activity level:")
        print("a - Sedentary\nb - Moderately Active\nc - Active")
        print("Please tell us your activity level")
        activity_level = input("a, b or c\n")
        if activity_level == "a" or activity_level == "b" \
                or activity_level == "c":
            return activity_level
        else:
            raise ValueError(
                "Please choose a, b or c:"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        get_activity_level()


def get_recc_calories(gender, age, activity_level):
    """
    Get recommended calories depending on age, gender and activity level
    """
    if gender == "f":
        if age <= 30:
            if activity_level == "a":
                recc_calories = 1800
                return recc_calories
            elif activity_level == "b":
                recc_calories = 2000
                return recc_calories
            elif activity_level == "c":
                recc_calories = 2400
                return recc_calories

        elif age > 30 and age <= 50:
            if activity_level == "a":
                recc_calories = 1800
                return recc_calories
            elif activity_level == "b":
                recc_calories = 2000
                return recc_calories
            elif activity_level == "c":
                recc_calories = 2200
                return recc_calories

        elif age > 50:
            if activity_level == "a":
                recc_calories = 1600
                return recc_calories
            elif activity_level == "b":
                recc_calories = 1800
                return recc_calories
            elif activity_level == "c":
                recc_calories = 2200
                return recc_calories

    if gender == "m":
        if age <= 30:
            if activity_level == "a":
                recc_calories = 2400
                return recc_calories
            elif activity_level == "b":
                recc_calories = 2600
                return recc_calories
            elif activity_level == "c":
                recc_calories = 3000
                return recc_calories

        elif age > 30 and age <= 50:
            if activity_level == "a":
                recc_calories = 2200
                return recc_calories
            elif activity_level == "b":
                recc_calories = 2400
                return recc_calories
            elif activity_level == "c":
                recc_calories = 2800
                return recc_calories

        elif age > 50:
            if activity_level == "a":
                recc_calories = 2000
                return recc_calories
            elif activity_level == "b":
                recc_calories = 2200
                return recc_calories
            elif activity_level == "c":
                recc_calories = 2400
                return recc_calories


def workout_plan(recommendation, name):
    """
    Get Workout plan from workouts.json
    """
    print("\n----------------------------------------------------")
    print(f"{name} we will now give you a workout plan")
    print(f"based on your recommmendation of {recommendation}")
    print("The plan is a 3 day workout plan split into:")
    print("Upper Body\nLower Body\nFull Body")
    print("You can adjust the workouts as necessary to")
    print("Best suit your needs")
    print("----------------------------------------------------\n")

    if recommendation == "weight gain":
        weight_gain_session_print()
    elif recommendation == "maintenance":
        maintenance_session_print()
    elif recommendation == "weight loss":
        weight_loss_session_print()


def weight_gain_session_print():
    """
    Prints the gain weight sessions
    """
    # Open workouts.json file
    with open("workouts.json", "r") as f:
        data = json.load(f)

    # gets the gain weight sessions dictionary
    weight_plan = data["Reccommendation"][0]

    # gets the gain weight sessions
    weight_sessions = weight_plan["weight gain"][0]

    print("----------------------------------------------------")
    print("Upper Body:")
    for i in weight_sessions["Upper body"]:
        print(i)

    print("----------------------------------------------------")
    print("Lower Body:")
    for i in weight_sessions["Lower body"]:
        print(i)

    print("----------------------------------------------------")
    print("Full Body:")
    for i in weight_sessions["Full body"]:
        print(i)

    print("----------------------------------------------------")


def maintenance_session_print():
    """
    Prints the maintenance weight sessions
    """
    # Open workouts.json file
    with open("workouts.json", "r") as f:
        data = json.load(f)

    # gets the maintenance weight sessions dictionary
    weight_plan = data["Reccommendation"][1]

    # gets the maintenance weight sessions
    weight_sessions = weight_plan["maintenance"][0]

    print("----------------------------------------------------")
    print("Upper Body:")
    for i in weight_sessions["Upper body"]:
        print(i)

    print("----------------------------------------------------")
    print("Lower Body:")
    for i in weight_sessions["Lower body"]:
        print(i)

    print("----------------------------------------------------")
    print("Full Body:")
    for i in weight_sessions["Full body"]:
        print(i)

    print("----------------------------------------------------")


def weight_loss_session_print():
    """
    Prints the weight loss sessions
    """
    # Open workouts.json file
    with open("workouts.json", "r") as f:
        data = json.load(f)

    # gets the weight loss sessions dictionary
    weight_plan = data["Reccommendation"][2]

    # gets the weight loss sessions
    weight_sessions = weight_plan["weight loss"][0]

    print("----------------------------------------------------")
    print("Upper Body:")
    for i in weight_sessions["Upper body"]:
        print(i)

    print("----------------------------------------------------")
    print("Lower Body:")
    for i in weight_sessions["Lower body"]:
        print(i)

    print("----------------------------------------------------")
    print("Full Body:")
    for i in weight_sessions["Full body"]:
        print(i)

    print("----------------------------------------------------")


def main():
    welcome()
    name = get_name()
    recommendation = bmi(name)
    recc_calories(name, recommendation)
    workout_plan(recommendation, name)


if __name__ == '__main__':
    main()
