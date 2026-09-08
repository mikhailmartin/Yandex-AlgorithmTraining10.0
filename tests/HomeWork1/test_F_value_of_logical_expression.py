import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.F_value_of_logical_expression import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1|(0&0^1)"],
            1,
            id="example1",
        ),
        param(
            ["!1|0&0^0&0|1&(0)"],
            0,
            id="test3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
