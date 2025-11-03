import pytest
from app.operations import Operation

def test_operation_not_implemented():
    op = Operation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)
