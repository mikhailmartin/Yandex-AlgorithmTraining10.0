import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.J_median import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 5 2 4 3",
            ],
            [1, 1, 2, 2, 3],
            id="example1",
        ),
        param(
            [
                "7",
                "10 1 2 3 9 5 8",
            ],
            [10, 1, 2, 2, 3, 3, 5],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
