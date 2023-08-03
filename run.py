


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
    print(f"With this result we recommend that your focus is on {recommendation}")
    print("----------------------------------------------------\n")

    return result


def recc_calories(name, bmi):
    print("----------------------------------------------------")
    print("Next we will calculate your recommended calories")
    print("We will do this by getting your gender, age and activity level")
    print("and creating a recommendation based on this")
    print("----------------------------------------------------\n")
    # get gender & validate
    print("Firstly please tell us your gender\nm - male\nf - female")
    while True:
        gender = input("Input your gender:\n")
        if validate_gender(gender):
            break

    # get age & validate
    while True:
        age = input("Firstly please tell us your age from 18-100:\n")
        if validate_age(age):
            break
    age = int(age)
    print(age)
    # get activity level and validate
    print("\nActivity level is your total amount of daily physical activity")
    print("It is split into three levels:")
    print("Sedentary is inactive where your only activity is daily life\n")
    print("Moderately active is at least 60 mins 3 days a week")
    print("of moderately intense excercise for  per week\n")
    print("Active is at least 60 mins 5 days a week")
    print("of moderately intense to intense exercise per week\n")
    while True:
        
        print("Choose your activity level:")
        print("a - Sedentary\nb - Moderately Active\nc - Active")

        activity_level = input("Next please tell us your activity level a, b or c\n")

        if validate_activity_level(activity_level):
            break
    print(activity_level)


def validate_gender(gender):
    try:
        if gender == "m" or gender == "f":
            pass
        else:
            raise ValueError(
                "Please choose m for male or f for female"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False


def validate_activity_level(level):
    try: 
        if level == "a" or level == "b" or level == "c":
            pass
        else:
            raise ValueError(
                "Please choose a, b or c"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False


def validate_age(age):
    try:
        age = int(age)
        if age >= 18 and age <= 100:
            pass
        else:
            raise ValueError(
                "Age must only be numbers and between 18 & 100"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


def main():
    user = get_name()
    body_mass_index_result = bmi(user)
    recc_calories(name, body_mass_index_result)


print("Welcome to Fit Check!")
print("We will ask you some questions, do some calculations and then give some recommendations")
print("But first...\n")
main()
