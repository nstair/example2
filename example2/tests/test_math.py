
import pytest
import numpy as np

import example2 as e2

#@pytest.mark.paramatrize('n, answer', [(0,1), (1,2)])

def test_one():
    assert e2.math.one(1) == 1.0

def test_pi():
    val = e2.math.pi(1000000)
    assert val == pytest.approx(3.14159, 0.001)
