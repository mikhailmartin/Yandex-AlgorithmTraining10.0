import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork3.I_heap_sort_number_of_exchanges import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "5",
                "1 2 3 4 5",
            ],
            3,
            id="example1",
        ),
        param(
            [
                "5",
                "5 4 3 2 1",
            ],
            0,
            id="example2",
        ),
        param(
            [
                "5",
                "5 3 1 2 4",
            ],
            1,
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
