
def name():
    """
    Gets user name and validates input
    """
    while True:
        name = input("Please Enter your first name:\n")

        if validate_name(name):
            break

    return name


def validate_name(name):
    """
    Validates user input as only letters and less than 20 characters
    """

    try:
        if str.isalpha(name) and len(name) < 20:
            pass
        else:
            raise ValueError(
                f"Name must only be letters and less than 20 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


def bmi(name):
    """
    Calculates user BMI by getting height and weight and validates both
    """
    print(f"Welcome {name}\n")
    print("Firstly we will calculate your Body Mass Index (BMI)")
    print("This figure is used to estimate your total amount of body fat.")
    print("It is only an approximate measure of the")
    print("best weight for your health.\n")

    # get height & validate
    while True:
        height = input("Firstly please enter your height in centimeters e.g. 180 (Do not include cm):\n")
        if validate_h_or_w(height, "Height"):
            break
    height = int(height)

    # get weight & validate
    while True:
        weight = input("Now please enter your weight in kg e.g. 80 (Do not include kg):\n")
        if validate_h_or_w(weight, "Weight"):
            break
    weight = int(weight)

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # give results
    result = bmi_result(bmi, name)

    return result


def validate_h_or_w(data, type):
    """
    Validates height and weight to ensure in correct form
    """
    unit = ""
    if type == "Height":
        unit = "cm"
    elif type == "Weight":
        unit = "kg"
    else:
        print("we have encountered an error... Restarting")
        main()

    try:
        data = int(data)
        if data < 300:
            pass
        else:
            raise ValueError(
                f"{type} must only be numbers and less than 300{unit}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


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

    print(f"\n{name}, your BMI is {bmi}\n")
    print(f"This result classifies you as {result}")
    print(f"With this result we recommend that your focus is on {recommendation}\n")

    return result


def recc_calories(name, bmi):
    print("Next we will calculate your recommended calories")
    print("We will do this by getting your age and activity level")
    print("and creating a recommendation based on this")

    # get age & validate
    while True:
        age = input("Firstly please tell us your age from 18-100\n")
        if validate_age(age):
            break
    age = int(age)
    
    # get activity level and validate
    while True:

        activity_level = input("Next please tell us your activity level a, b or c\n")
        if validate_age(age):
            break
    age = int(age)
    print(age)


def validate_age(age):
    try:
        age = int(age)
        if age >= 18 or age <= 100:
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
    user = name()
    body_mass_index_result = bmi(user)
    recc_calories(name, body_mass_index_result)


print("Welcome to Fit Check!")
print("We will ask you some questions, do some calculations and then give some recommendations")
print("But first...\n")
main()
