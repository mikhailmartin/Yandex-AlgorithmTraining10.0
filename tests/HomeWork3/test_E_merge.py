import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.E_merge import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 3 5 5 9",
                "3",
                "2 5 6",
            ],
            [1, 2, 3, 5, 5, 5, 6, 9],
            id="example1",
        ),
        param(
            [
                "1",
                "0",
                "0",
                "",
            ],
            [0],
            id="example2",
        ),
        param(
            [
                "0",
                "",
                "1",
                "0",
            ],
            [0],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
