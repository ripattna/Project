calculation_to_units = 24
name_of_unit = "hours"


# Function with return type
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}."


user_input = days_to_units(20)
print(user_input)
