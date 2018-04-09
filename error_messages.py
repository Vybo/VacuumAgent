def value_integer_error():
    print("[Loading Error] Supplied wrong value for parameter '-n'. Expected value is UNSIGNED INTEGER.")

def value_boolean_error():
    print("[Loading Warning] Supplied wrong value for parameter '-n'. Expected value is BOOLEAN.")

def required_parameter_missing(parameter):
    print("[Loading Error] Required parameter %(parameter)s not supplied." %{"parameter": parameter})


def wrong_coordinate(coordinate):
    print("[Loading Error] Supplied unsupported coordinate %(coordinate)s. Supported format is: a0 [letter][unsigned integer]." %{"coordinate": coordinate})


def coordinate_over_n(coordinate, range):
    print("[Loading Error] Supplied coordinate %(coordinate)s is outside maze range %(range)i." %{"coordinate": coordinate, "range": range})


def coordinates_over_n(range):
    print("[Loading Error] Supplied coordinates outside maze range %(range)i." %{"range": range})
