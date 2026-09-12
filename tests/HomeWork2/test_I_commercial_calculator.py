import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.I_commercial_calculator import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "10 11 12 13",
            ],
            "4.60",
            id="example1",
        ),
        param(
            [
                "2",
                "1 1",
            ],
            "0.10",
            id="test3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
