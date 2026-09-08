import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.D_postfix_notation import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["8 9 + 1 7 - *"],
            -102,
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
