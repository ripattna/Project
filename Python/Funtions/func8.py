calculation_to_units = 24
name_of_unit = "hours"


# Function with return type
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}."


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a negative value!,So no conversion for you!")
    else:
        print("Your user input is not a valid number,Don't run the program.")


user_input = input("Hey User,Enter a number of days and I will convert it to hours!:\n")

validate_and_execute()
