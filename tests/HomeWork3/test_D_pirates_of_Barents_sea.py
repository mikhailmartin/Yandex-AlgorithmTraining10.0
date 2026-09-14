import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.D_pirates_of_Barents_sea import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3",
                "1 2",
                "3 3",
                "1 1",
            ],
            3,
            id="example1",
        ),
        param(
            [
                "4",
                "1 4",
                "2 2",
                "3 2",
                "4 2",
            ],
            2,
            id="custom1",
        )
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
