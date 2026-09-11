import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork2.E_goblins_and_shamans import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "7",
                "+ 1",
                "+ 2",
                "-",
                "+ 3",
                "+ 4",
                "-",
                "-",
            ],
            ["1", "2", "3"],
            id="example1",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
