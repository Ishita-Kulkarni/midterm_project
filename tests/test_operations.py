# tests/test_operations.py
import pytest
from app.operations import get_operation
from app.exceptions import OperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 1, 2, 3),
    ("subtract", 5, 3, 2),
    ("multiply", 2, 3, 6),
    ("power", 2, 3, 8),
    ("abs_diff", 5, 2, 3),
])

def test_basic_ops(op, a, b, expected):
    operation = get_operation(op)
    assert operation.execute(a, b) == expected


@pytest.mark.parametrize("op,a,b,expected", [
    ("root", 27, 3, 3),
    ("modulus", 10, 3, 1),
    ("int_divide", 10, 3, 3),
    ("percent", 2, 4, 50),
])
def test_more_ops(op, a, b, expected):
    operation = get_operation(op)
    assert operation.execute(a, b) == expected
    operation = get_operation(op)
    assert operation.execute(a, b) == expected

def test_divide_zero():
    op = get_operation("divide")
    with pytest.raises(OperationError):
        op.execute(1, 0)
