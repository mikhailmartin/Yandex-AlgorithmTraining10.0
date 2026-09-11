import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.D_beach_volleyball import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "1 3 2 4",
                "1",
                "3",
            ],
            [(3, 4)],
            id="example1",
        ),
        param(
            [
                "4",
                "2 1 4 3",
                "3",
                "1",
                "5",
                "2",
            ],
            [(2, 1), (4, 2), (2, 4)],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
