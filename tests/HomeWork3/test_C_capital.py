import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.C_capital import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "8",
                "0 0",
                "1 0",
                "2 0",
                "0 1",
                "2 1",
                "0 2",
                "1 2",
                "2 2",
            ],
            (1, 1),
            id="example1",
        ),
        param(
            [
                "4",
                "0 0",
                "1 1",
                "0 1",
                "1 0",
            ],
            (-1, 0),
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
