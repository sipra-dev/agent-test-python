def _validate_operands(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("boolean operands are not supported")


def add(a, b):
    _validate_operands(a, b)
    return a + b


def subtract(a, b):
    _validate_operands(a, b)
    return a - b


def divide(a, b):
    _validate_operands(a, b)
    return a / b
