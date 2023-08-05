# Testing for Fit Check

Return to [README](/workspaces/Fit-Check/README.md)

## Code Validation 

All python code was validated using [CI Python Linter](https://pep8ci.herokuapp.com/) and no errors were found

![CI Python Linter result](/docs/images/validator-result.jpg)

## Manual Testing

Manual testing was conducted on all the elements of the program to ensure all were working as expected and that no bugs were found 

### Welcome screen

| Step        | Description  | Expected Result  | Actual Result | Pass / Fail | 
| ------------- |:-------------:| -----:        | ------------- |:-------------:| 
| 1           | Deployed Website  | The welcome screen loads with no issues | Welcome Screen loads with no issues      | Pass | 
|2            | User Input    |   User Enters name accepting only one word less than 20 characters long and only consisting of letters | Name is accepted and succesfully validated     | Pass  |  

### BMI Testing

| Step        | Description  | Expected Result  | Actual Result | Pass / Fail | 
| ------------- |:-------------:| -----:        | ------------- |:-------------:| 
| 1 | User Height Input| User enters height and it is validated that is only numbers and less than 300| Height validated successfully |Pass| 
| 2 |User Weight Input| User enters weight and it is validated that is only numbers and less than 300| Weight validated succcessfully |Pass| 

### Recommended Calories Testing 

| Step        | Description  | Expected Result  | Actual Result | Pass / Fail | 
| ------------- |:-------------:| -----:        | ------------- |:-------------:| 
| 1 |User Gender Input| User enters their gender either m or f and that is validated to be only those inputs| Input validated successfully |Pass| 
| 2 |User Age Input| User enters their age only numbers between 18-100 |Age validated successfully |Pass| 
| 3 |User Activity Level Input| User enters their activity level either a , b or c | Activity level validated successfully |Pass| 

### Restart Section

| Step        | Description  | Expected Result  | Actual Result | Pass / Fail | 
| ------------- |:-------------:| -----:        | ------------- |:-------------:|
| 1 |Restart Input| User chooses to restart or end the program depending on input y or n| Input is validated and results in user choice |Pass|

## User Stories Testing 

I would like to find out my BMI without having to do any calculations
-  Users BMI is successfully calculated and a recommendation is given using the users inputs

I would like to find out my daily recommended calories without having to do any calculations
- Users recommended calories is successfully calculated and a recommendation is given using the users inputs

I would like to see errors and reasoning if there is issues with my inputs
- If an input was given incorrectly the user was informed of the issue

I would like to get a recommended weekly workout plan that suits my needs
- Using the users input a weekly workout plan was recommended to the user

## Resolved Bug

When initially validating code all the validation functions were set up as follows:
```
def get_name():
    """
    Validates user input as only letters and less than 20 characters
    """

    try:
        name = input("Please Enter your first name:\n")
        if name.isalpha() and len(name) < 20:
            return name
        else:
            raise ValueError(
                f"Name must only be letters and less than 20 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        get_name()
```

This resulted in a returned variable of None if an incorrect input was first inputted.

To combat this issue a different structure was implemented:

```
def get_name():
    """
    Validates user input as only letters and less than 20 characters
    """

    while True:
        name = input("Please Enter your first name:\n")
        if validate_name(name):
            break

    return name


def validate_name(name):
    try:
        if name.isalpha() and len(name) < 20:
            return name
        else:
            raise ValueError(
                f"Name must only be letters and less than 20 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True
```

This structure resolved this bug and inputs were then properly validated



Return to [README](/workspaces/Fit-Check/README.md)