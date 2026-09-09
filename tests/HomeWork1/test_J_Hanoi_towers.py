import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.J_Hanoi_towers import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["2"],
            [
                (1, 1, 2),
                (2, 1, 3),
                (1, 2, 3),
            ],
            id="example1",
        ),
        param(
            ["3"],
            [
                (1, 1, 3),
                (2, 1, 2),
                (1, 3, 2),
                (3, 1, 3),
                (1, 2, 1),
                (2, 2, 3),
                (1, 1, 3),
            ],
            id="example2",
        ),
        param(
            ["1"],
            [
                (1, 1, 3),
            ],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
