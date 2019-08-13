"""
Unit and regression test for the example2 package.
"""

# Import package, test suite, and other packages as needed
import example2
import pytest
import sys

def test_example2_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "example2" in sys.modules
