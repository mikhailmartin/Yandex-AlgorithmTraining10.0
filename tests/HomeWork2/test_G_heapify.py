import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.G_heapify import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "2",
                "0 10000",
                "1",
            ],
            [10000],
            id="example1",
        ),
        param(
            [
                "14",
                "0 1",
                "0 345",
                "1",
                "0 4346",
                "1",
                "0 2435",
                "1",
                "0 235",
                "0 5",
                "0 365",
                "1",
                "1",
                "1",
                "1",
            ],
            [345, 4346, 2435, 365, 235, 5, 1],
            id="example2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
