import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.A_partition import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 9 4 2 3",
                "3"
            ],
            (2, 3),
            id="example1",
        ),
        param(
            [
                "0",
                "",
                "0",
            ],
            (0, 0),
            id="example2",
        ),
        param(
            [
                "1",
                "0",
                "0",
            ],
            (0, 1),
            id="example3",
        ),
        param(
            [
                "1",
                "0",
                "1",
            ],
            (1, 0),
            id="custom1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
