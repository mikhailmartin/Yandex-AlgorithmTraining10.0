import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.B_minimal_CBS import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "6",
                "()[]",
                "([(",
            ],
            "([()])",
            id="example1",
        ),
        param(
            [
                "6",
                "][)(",
                "([",
            ],
            "([][])",
            id="example2",
        ),
        param(
            [
                "4",
                "(][)",
                "()[]",
            ],
            "()[]",
            id="example3",
        ),
        param(
            [
                "6",
                "])([",
                "",
            ],
            "()()()",
            id="test4",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
