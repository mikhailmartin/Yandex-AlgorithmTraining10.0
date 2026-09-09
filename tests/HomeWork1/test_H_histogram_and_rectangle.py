import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.H_histogram_and_rectangle import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["7 2 1 4 5 1 3 3"],
            8,
            id="example1",
        ),
        param(
            ["4 1000 1000 1000 1000"],
            4000,
            id="test2",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
