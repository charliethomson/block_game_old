DEFAULT_ARGS = {
    "BLOCK_ID": None,
    "BLOCK_NAME": None,
    "BREAK": None,
    "DROPS_ITEM": None,
    "SPRITE_PATH": None,
    "GRAVITY": None,
}


class ParserError(Exception):
    pass


def _fix_vars(vars: dict):
    new = {}
    print(vars)
    for key in list(vars.keys()):
        value = vars[key]
        if value.lower() == "false":
            new_value = False
        elif value.lower() == "true":
            new_value = True
        elif value.lower() == "none":
            new_value = None
        elif "." in value:
            if "/" in value:
                new_value = value
            else:
                new_value = int(value.split(".")[0])
        elif value.isnumeric():
            new_value = int(value)
        else:
            new_value = value
        new[key.upper()] = new_value
    final = _add_missing_args(new)
    return final


def _add_missing_args(vars: dict):
    for key in list(DEFAULT_ARGS.keys()):
        if key not in list(vars.keys()):
            vars[key] = DEFAULT_ARGS[key]
    return vars


def parse_block(file_path: str):
    assert isinstance(
        file_path, str
    ), f"File path type mismatch {type(file_path)} -> {type('')}"

    # Read the data from the keybinds file
    with open(file_path, "r") as bindings:
        data = bindings.read()

    variable_name_dec, variable_val_dec = False, False
    variable_name, variable_val = "", ""
    variables = {}
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
        else:
            raise ParserError(f"Encountered unexpected character {char}")

    _fix_vars(variables)
    return variables


def test():
    print(parse_block("./resources/blocks/air"))
