import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.E_value_of_arithmetic_expression import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1+(2*2 - 3)"],
            2,
            id="example1",
        ),
        param(
            ["1+a+1"],
            "WRONG",
            id="example2",
        ),
        param(
            ["1 1 + 2"],
            "WRONG",
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
