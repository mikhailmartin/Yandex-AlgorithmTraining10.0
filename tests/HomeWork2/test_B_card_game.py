import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.B_card_game import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["1 3 5 7 9", "2 4 6 8 0"],
            "second 5",
            id="example1",
        ),
        param(
            ["2 4 6 8 0", "1 3 5 7 9"],
            "first 5",
            id="example2",
        ),
        param(
            ["1 7 3 9 4", "5 8 0 2 6"],
            "second 23",
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
