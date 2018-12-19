def convert_string(string: str):
    # Integers
    if string.isnumeric():
        return int(string)
    if "." in string and [item.isnumeric() for item in string.split(".")]:
        return float(string)

    convs = {"true": True, "false": False, "none": None}
    if string.lower() in list(convs.keys()):
        return convs[string.lower()]

    else:
        return string


def string_to_matrix(string: str):
    matrix = []

    current_item, current_array = "", []
    item, array = False, False
    for next_index, char in enumerate(string):
        next_ = next_index + 1 if next_index < len(string) - 1 else None
        if item:
            print(char)
            if char == "[":
                array = True
            if char == "]":
                array = matrix.append(current_array)
            elif char == ",":
                if array:
                    matrix.append(current_array)
                    array, item = False, False
                else:
                    current_array.append(current_item)
            else:
                current_item += char

        elif char == "[":
            item = True

    return matrix


def _fix_vars(vars: dict):
    new = {}
    for key in list(vars.keys()):
        value = vars[key]
        # if "[" in value:
        #     new[key.upper()] = string_to_matrix(value)


def parse_map(map_file: str):

    # Read the data from the map file
    with open(map_file, "r") as map_:
        data = map_.read()

    variable_name_dec, variable_val_dec = False, False
    variable_name, variable_val = "", ""
    variables = {}

    for char in data:
        # If we're declaring a variable
        if variable_name_dec:
            # add the character to the variable name until you come
            # across an = then start getting the value, passing any
            # spaces, newlines, or tabs
            if char == "=":
                variable_name_dec = False
                variable_val_dec = True
            elif char in ("\n", "\t", " "):
                continue
            else:
                variable_name += char
                continue

        # if we're getting the value
        if variable_val_dec:
            # add the character to the value until you come across
            # a ; then stop looking for a value, add the variable
            #  and the value to the dictionary, and reset them both
            if char == ";":
                variable_val_dec = False
                variables[variable_name] = variable_val
                variable_name, variable_val = "", ""
            elif char in ("\n", "\t"):
                continue
            else:
                variable_val += char
                continue

        # skip newlines and tabs
        if char in ["\n", "\t"]:
            continue
        # if we come across a :, start getting the variable name
        elif char == ":":
            variable_name_dec = True

