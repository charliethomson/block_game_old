from os.path import exists as file_exists
from pyglet.window import key as keys

# General parser for my file format


class ParserError(Exception):
    pass


class IncorrectGivenDataError(ParserError):
    pass


class ParserUnexpectedCharacterError(ParserError):
    pass


class UnfoundKeycodeError(ParserError):
    pass


def _fix_keybinds(vars: dict):
    """
    Makes the keys how the program will expect them, gets the values from pyglet for key codes
        P.S, this function could be like 5 lines but errors so it's 30
    """
    assert isinstance(
        vars, dict
    ), f"Error fixing keybind vars, type mismatch; {type(vars)} -> {dict}"
    new = {}
    for key in list(vars.keys()):

        ## Error Checking ##
        if not isinstance(key, str):
            raise ParserError(
                f"Command incorrect - type mismatch; {type(key)} -> {str}"
            )
        for char in key:
            if char.isnumeric():
                raise ParserError(
                    f"Command incorrect - command {key} contains bad symbol {char}"
                )
        if not hasattr(keys, vars[key]):
            raise UnfoundKeycodeError
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


def _fix_types(vars: dict):

    # I don't know a situation in which this would happen, but checks ya know
    assert isinstance(
        vars, dict
    ), f"Unable to fix var types, `vars` incorrect type: {type(vars)}"

    new_vars = {}
    for key in list(vars.keys()):
        value = vars[key]
        # boolean
        if value in (True, False, None):
            new_vars[key.upper()] = value
        elif "-" in value and _check_negative(value):
            if _check_numeric(value):
                new_vars[key.upper()] = float(value)
            else:
                new_vars[key.upper()] = int(value)
        # float
        elif "." in value and _check_numeric(value):
            new_vars[key.upper()] = float(value)
        # int
        elif value.isnumeric():
            new_vars[key.upper()] = int(value)
        # list / matrix, as deep as you want, keep the brackets even though
        elif "[" in value:
            new_vars[key.upper()] = _string_to_list(value)
        else:
            new_vars[key.upper()] = str(value)
    return new_vars


def _check_missing_vars(vars: dict, reqds: list, defaults: list):

    assert isinstance(
        vars, dict
    ), f"Unable to check variables, `vars` incorrect type: {type(vars)}"

    if reqds:

        if defaults == None:
            defaults = []
            [defaults.append(None) for _ in range(len(reqds))]
        elif len(defaults) < len(reqds):
            [defaults.append(None) for _ in range(len(reqds) - len(defaults))]

        for index in range(len(reqds)):
            current = reqds[index]
            if not current in list(vars.keys()):
                vars[current] = defaults[index]

    vars = _fix_types(vars)

    return vars


def _check_negative(string: str):
    for item in string.split("-"):
        if item == "":
            continue
        elif not item.isnumeric():
            return False
    return True


def _check_numeric(string: str):
    for item in (_.isnumeric() for _ in string.split(".")):
        if not item:
            return False
    return True


def _string_to_list(string: str) -> list:
    o, c = string.count("["), string.count("]")
    assert o == c, f"open / close bracket count mismatch (open: {o}, close: {c})"

    for index in range(1, len(string) - 1):
        last, current, next = string[index - 1], string[index], string[index + 1]
        if current + next == "][":
            surrounding = string[index - 10 : index + 10]
            raise SyntaxError(f"Missing comma between two brackets {surrounding}")

    x = []
    exec(f"x.append({string})")
    value = x[0]

    return value


def parse(
    user_input: str, reqds: list = None, defaults: list = None, given_data: str = None
):
    """
    MAIN PARSE FUNCTION

    ARGS: 
        `user_input` : String ; The file to be parsed, assumed to be 
                          formatted like: "./path/file", unix-style  
                          (one dot for current folder, two for one 
                          up, etc)
                             ; if you don't have a file to read from,
                               you can read from stdin, the `given_data`
                               kwarg, or a string using (respectively) 
                               `stdin`, `given`, or using the string as 
                               the `user_input` arg

    KWARGS:
        `reqds`      : list ; Required variable names, a list of strings
        `defaults`   : list ; If missing a variable name, it will set it
                              to the value at the same index as in reqds 
                              in this list, None if defaults is too short
                              or if it is not provided 
                            ; These lists are reliant on indexing, get it
                              right :)
        `given_data` :  str ; 
        `keybinds`   : bool ; whether or not it's parsing a keybinds file,
                              there's some special magic needed to do that
    """

    assert isinstance(
        user_input, str
    ), f"User input type mismatch: {type(user_input)} -> {str}"
    # stdin ; ask for the data from stdin :)
    if user_input == "stdin":
        data = input("Enter the data to be parsed: ")
    # given ; check that data was given, assign it if it is, raise an error otherwise
    elif user_input == "given":
        if not given_data:
            raise IncorrectGivenDataError(
                "Data cannot be parsed if it doesn't exist, no data given when expected"
            )
        data = given_data
    # directly given in a string ; the spec defines that it'll always (formatted correctly)
    # start with a colon and end with a semicolon, so we check for that, then assign the data
    elif user_input.startswith(":") and user_input.endswith(";"):
        data = user_input
    # here we assume it's a file path, so we check if the file exists then read the data
    else:
        assert file_exists(user_input), f"File {user_input} does not exist"

        with open(user_input, "r") as file_:
            data = file_.read()

    # Variable name declaration, variable value declaration
    varndec, varvdec = False, False
    # Variable name, variable value
    varn, varv = "", ""
    # Variables
    vars = {}

    # This part parses the data

    for char in data:
        if char in ["\n", "\t"]:
            continue
        if varndec:
            if char != "=":
                varn += char
                continue
            else:
                varndec = False
                varvdec = True
                continue
        if varvdec:
            if char != ";":
                varv += char
                continue
            else:
                varvdec = False
                vars[varn] = varv
                varn, varv = "", ""
                continue
        elif char == ":":
            varndec = True
            continue
        else:
            raise ParserUnexpectedCharacterError(
                f"Parser encountered unexpected character: {char}"
            )

    vars = _check_missing_vars(vars, reqds, defaults)
    return vars
