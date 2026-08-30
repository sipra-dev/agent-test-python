import pytest

from calculator import add, subtract, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.parametrize(
    ("operation", "left", "right"),
    [
        (add, True, 3),
        (add, 2, False),
        (subtract, False, 3),
        (subtract, 5, True),
        (divide, True, 2),
        (divide, 10, False),
    ],
)
def test_operations_reject_boolean_operands(operation, left, right):
    with pytest.raises(TypeError):
        operation(left, right)
