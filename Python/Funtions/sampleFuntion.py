print(f"20 days are {20*24} hours")
print(f"35 days are {35*24} hours")
print(f"50 days are {50*24} hours")

"""Using the Function"""
print("Using the Function")
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}.")


days_to_units(20)
days_to_units(35)
days_to_units(50)
