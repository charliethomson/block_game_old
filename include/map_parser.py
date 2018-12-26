from os.path import exists

class ParserError(Exception):
    pass


def _check_numeric(string):
    for item in (item.isnumeric() for item in string.split(".")):
        if not item:
            return False
    return True

def _check_vars(vars):
    reqd_vars = {
        "MAP_NAME": "World",
        "CREATION_TIME": '',
        "CREATION_DELTA_INIT": 1545472736,
        "MAP": None
    }

    for var in list(reqd_vars.keys()):
        # Check if each of the required variables is in the given vars, if 
        # one's missing, add it w/ the default value
        if var not in vars:
            vars[var] = reqd_vars[var]

    return vars

def _string_to_matrix(string: str):
    x = []
    exec(f"x.append({string})")
    return x[0]

def _convert_string(string: str):
    convs = {"true": True, "false": False, "none": None}
    
    if string.isnumeric():
        return int(string)
        
    elif "." in string and _check_numeric(string):
        return float(string)

    elif string.lower() in list(convs.keys()):
        return convs[string.lower()]

    elif "[" in string:
        return _string_to_matrix(string)

    else:
        return string


def _fix_vars(vars: dict):
    new = {}
    for key in list(vars.keys()):
        value = vars[key]
        # convert_string sets the types correctly to what they need to be
        new[key.upper()] = _convert_string(value)

    return new


def parse_map(map_file: str):

    if not exists(map_file):
        raise ParserError(f"map file {map_file} does not exist")

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
                continue
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

    variables = _fix_vars(variables)
    variables = _check_vars(variables)
    return variables

