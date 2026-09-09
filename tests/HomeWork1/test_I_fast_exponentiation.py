import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.I_fast_exponentiation import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["2", "1"],
            2,
            id="example1",
        ),
        param(
            ["2", "2"],
            4,
            id="example2",
        ),
        param(
            ["2", "3"],
            8,
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
