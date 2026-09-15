import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.G_merge_sort import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 5 2 4 3",
            ],
            [1, 2, 3, 4, 5],
            id="example1",
        ),
        param(
            [
                "1",
                "1",
            ],
            [1],
            id="custom1",
        ),
        param(
            [
                "2",
                "2 1",
            ],
            [1, 2],
            id="custom2",
        ),
        param(
            [
                "0",
                "",
            ],
            [],
            id="custom3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
