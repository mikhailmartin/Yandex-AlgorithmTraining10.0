import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.C_automated_warehouse import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "4",
                "1 3",
                "1 1",
                "3 1",
                "2 1",
                "2 2",
            ],
            [1, 1, 2, 3],
            id="example1",
        ),
        param(
            [
                "4",
                "1 2",
                "1 1",
                "2 1",
                "3 1",
                "4 1",
            ],
            [1, 2, 3, 4],
            id="example2",
        ),
        param(
            [
                "1",
                "1 4",
                "1 1",
            ],
            [1],
            id="example3",
        ),
        param(
            [
                "43",
                "3 2",
                "4 21",
                "1 13",
                "2 48",
                "1 100",
                "2 74",
                "1 61",
                "2 42",
                "2 25",
                "1 85",
                "4 62",
                "4 86",
                "3 2",
                "2 10",
                "1 21",
                "2 85",
                "3 55",
                "2 98",
                "1 51",
                "2 28",
                "4 5",
                "1 71",
                "2 5",
                "2 56",
                "1 36",
                "4 13",
                "4 100",
                "3 15",
                "3 63",
                "1 9",
                "3 49",
                "4 96",
                "4 49",
                "4 25",
                "1 77",
                "2 29",
                "4 34",
                "1 94",
                "3 61",
                "3 72",
                "2 34",
                "3 19",
                "2 90",
                "2 22",
            ],
            [21, 14, 48, 101, 74, 64, 42, 25, 87, 62, 86, 2, 10, 23, 85, 55, 98, 51, 28, 6, 71, 5, 56, 36, 13, 100, 15, 63, 9, 49, 96, 50, 26, 77, 29, 35, 94, 61, 72, 34, 19, 90, 22],
            id="test17"
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
