def parse_map(map_file: str):

    with open(map_file, "r") as map_:
        data = map_.read()

    variable_name_dec, variable_val_dec = False, False
    variable_name, variable_val = "", ""
    variables = {}

    for char in data:
        if variable_name_dec:
            if char == "=":
                variable_name_dec = False
                variable_val_dec = True
            else:
                variable_name += char
                continue
        if variable_val_dec:
            if char == ";":
                variable_val_dec = False
                variables[variable_name] = variable_val
                variable_name, variable_val = "", ""
            else:
                variable_val += char
                continue

        if char in ["\n", "\t"]:
            continue
        elif char == ":":
            variable_name_dec = True

