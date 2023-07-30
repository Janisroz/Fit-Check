
def name():
    """
    Gets user name and validates input
    """
    while True:
        name = input("Please Enter your first name:\n")
        name = name.lower()

        if validate_name(name):
            print("name is valid")
            break

    return name


def validate_name(name):
    try:
        if str.isalpha(name) and len(name)< 20:
            print("String is good")
        else:
            raise ValueError(
                f"Name must only be letters and less than 20 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True

def main():
    name()


print("Welcome to Fit Check!")
print("We will ask you some questions, do some calculations and then give some recommendations")
print("But first...\n")
main()