calculation_to_units = 24
name_of_unit = "hours"


# Function with 2 arguments(num_of_days, custom_message)
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}.")
    print(custom_message)


def scope_check(num_of_days):
    my_var = "Variable inside the function."
    print(my_var)               # Internal Variable
    print(name_of_unit)         # Global Variable
    print(num_of_days)          # Local Variable


scope_check(20)
