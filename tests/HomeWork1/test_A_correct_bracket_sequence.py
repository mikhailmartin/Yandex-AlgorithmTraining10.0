import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork1.A_correct_bracket_sequence.main import main


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            ["()[]"],
            "yes",
            id="example1",
        ),
        param(
            ["([)]"],
            "no",
            id="example2",
        ),
        param(
            ["("],
            "no",
            id="example3",
        ),
    ],
)
def test_main(lines, expected):
    assert main(lines) == expected
