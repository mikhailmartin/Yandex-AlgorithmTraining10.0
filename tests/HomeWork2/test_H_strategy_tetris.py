import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.H_strategy_tetris import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "3 4",
                "1 2",
                "2 2",
                "3 2",
            ],
            (2, [2, 1, 3]),
            id="example1",
        ),
        param(
            [
                "10 100",
                "76 25",
                "17 84",
                "1 16",
                "40 45",
                "1 66",
                "1 17",
                "67 9",
                "18 22",
                "1 100",
                "85 16",
            ],
            (4, [3, 2, 5, 7, 1, 9, 6, 8, 4, 10]),
            id="test3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
