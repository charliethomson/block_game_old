import pyglet


class ParserError(Exception):
    pass


def _fix_vars(vars: dict):
    """
    Makes the keys how the program will expect them, gets the values from pyglet for key codes
        P.S, this function could be like 5 lines but errors so it's 30
    """
    assert isinstance(
        vars, dict
    ), f"Error fixing keybind vars, type mismatch; {type(vars)} -> {type({})}"
    new = {}
    for key in list(vars.keys()):

        ## Error Checking ##
        if not isinstance(key, str):
            raise ParserError(
                f"Command incorrect - type incorrect {key}, got: {type(key)} expected: {type('')}"
            )
        for char in key:
            if char.isnumeric():
                raise ParserError(
                    f"Command incorrect - command {key} contains bad symbol {char}"
                )
        ## /Error Checking ##

        # Getting the keycode from pyglet.window.key, and adding it to the new dictionary
        new[key.upper()] = getattr(pyglet.window.key, vars[key])

    ## Error Checking ##
    for value in list(new.values()):
        if not isinstance(value, int):
            raise ParserError(
                f"Keybind translation failed, check ./saves/<save>/keybinds for errors: {value}"
            )
    ## /Error Checking ##
    return new


def parse_bindings(file_path: str):
    assert isinstance(
        file_path, str
    ), f"File path type mismatch {type(file_path)} -> {type('')}"

    # Read the data from the keybinds file
    with open(file_path, "r") as bindings:
        data = bindings.read()

    variable_name_dec, variable_val_dec = False, False
    variable_name, variable_val = "", ""
    variables = {}
    # This is the actual parsing part, it just follows the stuff I
    # outline in ./help_dox/keybinds-guide.txt, imports the data
    # into memory, cleans it up, and returns it.
    for char in data:
        if variable_name_dec:
            if char != "=":
                variable_name += char
                continue
            else:
                variable_name_dec = False
                variable_val_dec = True
                continue
        if variable_val_dec:
            if char != ";":
                variable_val += char
                continue
            else:
                variable_val_dec = False
                variables[variable_name] = variable_val
                variable_name, variable_val = "", ""
                continue
        if char == "\n":
            continue
        elif char == ":":
            variable_name_dec = True
            continue
        else:
            raise ParserError(f"Encountered unexpected character {char}")

    variables = _fix_vars(variables)
    return variables
