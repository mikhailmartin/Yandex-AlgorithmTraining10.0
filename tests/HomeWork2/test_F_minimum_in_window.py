import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.F_minimum_in_window import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7 3",
                "1 3 2 4 5 3 1",
            ],
            [1, 2, 2, 3, 1],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
