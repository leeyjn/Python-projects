unit_selection = input("Welcome to Unit Converter, select the unit you want to convert\n "
                       "(1)Days \n (2)Hours \n (3)Minutes \n (4)Seconds\n")
selection_method = int(unit_selection)


def selecting_units(method):
    if method == 1:
        return "days"
    elif method == 2:
        return "hours"
    elif method == 3:
        return "minutes"
    elif method == 4:
        return "seconds"
    else:
        return "error!"


num_units = input("How many " + str(selecting_units(selection_method)) + " to convert?\n")
number_of_units = int(num_units)

convert = input(" Choose your option: \n(1) calculation to days \n(2) calculation to hours \n(3) calculation to "
                "minutes "
                "\n(4) calculation to seconds\n")
convert_method = int(convert)


def converting_units(way):
    if way == 1:
        return "days"
    elif way == 2:
        return "hours"
    elif way == 3:
        return "minutes"
    elif way == 4:
        return "seconds"
    else:
        return "oops"


def calculation_to_seconds():
    if selection_method == 1:
        return number_of_units * 60 * 60 * 24
    elif selection_method == 2:
        return number_of_units * 60 * 60
    elif selection_method == 3:
        return number_of_units * 60
    elif selection_method == 4:
        return number_of_units * 1
    else:
        return "yikes"


def calculation_back_to_units():
    if convert_method == 1:
        return int(calculation_to_seconds()) / 86400
    elif convert_method == 2:
        return int(calculation_to_seconds()) / 3600
    elif convert_method == 3:
        return int(calculation_to_seconds()) / 60
    elif convert_method == 4:
        return int(calculation_to_seconds()) / 1
    else:
        return "oh no!"


def calculate_to_units():
    if convert_method == 1:
        return {number_of_units}, str(selecting_units(selection_method)), " are ", {calculation_back_to_units()}, \
               str(converting_units(convert_method))
    elif convert_method == 2:
        return {number_of_units}, str(selecting_units(selection_method)), " are ", {calculation_back_to_units()}, \
               str(converting_units(convert_method))
    elif convert_method == 3:
        return {number_of_units}, str(selecting_units(selection_method)), " are ", {calculation_back_to_units()}, \
               str(converting_units(convert_method))
    elif convert_method == 4:
        return {number_of_units}, str(selecting_units(selection_method)), " are ", {calculation_back_to_units()}, \
               str(converting_units(convert_method))
    else:
        return "error"


calculated_value = calculate_to_units()
print(calculated_value)
