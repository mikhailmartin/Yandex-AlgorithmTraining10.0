import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.G_great_Lineland_migration import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["10", "1 2 3 2 1 4 2 5 3 1"],
            [-1, 4, 3, 4, -1, 6, 9, 8, 9, -1],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
