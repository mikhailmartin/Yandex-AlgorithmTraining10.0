import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.J_heap_sort import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "1",
                "1",
            ],
            [1],
            id="example1",
        ),
        param(
            [
                "2",
                "3 1",
            ],
            [1, 3],
            id="example2",
        ),
        param(
            [
                "2",
                "1 3",
            ],
            [1, 3],
            id="custom1",
        ),
        param(
            [
                "3",
                "1 3 3 2",
            ],
            [1, 2, 3, 3],
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
        param(
            [
                "5",
                "5 4 3 2 1",
            ],
            [1, 2, 3, 4, 5],
            id="test3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
