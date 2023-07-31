
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
        if str.isalpha(name) and len(name)< 20:
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
    print("This figure is used to estimate your total amount of fat.")
    print("It is only an approximate measure of the best weight for your health.\n")
    
    # get height & validate
    while True :
        height = input("Firstly please enter your height in centimeters e.g. 180 (Do not include cm):\n")
        if validate_h_or_w(height, "Height"):
            break
    height = int(height)

    # get weight & validate
    while True :
        weight = input("Now please enter your weight in kg e.g. 80 (Do not include kg):\n")
        if validate_h_or_w(weight, "Weight"):
            break
    weight = int(weight)

    bmi = calculate_bmi(height, weight)
    print(bmi)

    
def validate_h_or_w(data, type):
    """
    Validates height and weight to ensure in correct form
    """
    unit = ""
    if type == "Height":
        unit = "cm"
    elif type == "Weight":
        unit = "kg"
    else :
        print("we have encountered an error... Restarting")
        main()  

    try:
        data = int(data)
        if data < 300 :
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




def main():
    user = name()
    body_mass_index = bmi(user)


print("Welcome to Fit Check!")
print("We will ask you some questions, do some calculations and then give some recommendations")
print("But first...\n")
main()