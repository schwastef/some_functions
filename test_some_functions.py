# This python script is used by pytest to run the test of the functions defined in "some_functions.py".
# It contains one test function for each function in "some_functions.py" with multiple assert
# statements testing multiple cases.

import numpy as np
import pytest

import some_functions as sf

a = -0.5 + np.sqrt(3) / 2 * 1j  # 120 degrees rotation operator


# Testfunction for "calc_parallel_impedance" function
def test_calc_parallel_impedance():
    assert sf.calc_parallel_impedance([4, 4, 4, 4]) == 1.0
    assert sf.calc_parallel_impedance([4 + 5j, 1 - 6j]) == pytest.approx(7.269 - 2.346j, abs=1e-3)


# Testfunction for "calc series impedance" function
def test_calc_series_impedance():
    assert sf.calc_series_impedance([4, 4, 4, 4]) == 16.0
    assert sf.calc_series_impedance([4 + 5j, 1 - 6j]) == pytest.approx(5.0 - 1j, abs=1e-3)


# Testfunction for "transformation" function
def test_transformation():
    assert sf.transformation(1, a**2, a) == pytest.approx(
        [0.0, 1.0, 0.0], abs=1e-3
    )  
    assert sf.transformation(1, a, a**2) == pytest.approx(
        [0.0, 0.0, 1.0], abs=1e-3
    )  
    assert sf.transformation(1, 1, 1) == pytest.approx(
        [1.0, 0.0, 0.0], abs=1e-3
    )  


# Testfunction for "inverse_transformation" function
def test_inverse_transformation():
    assert sf.inverse_transformation(0.0, 1.0, 0.0) == pytest.approx(  
        [1, -0.5 - 0.866j, -0.5 + 0.866j], abs=1e-3
    )
    assert sf.inverse_transformation(0.0, 0.0, 1.0) == pytest.approx(  
        [1, -0.5 + 0.866j, -0.5 - 0.866j], abs=1e-3
    )
    assert sf.inverse_transformation(1.0, 0.0, 0.0) == pytest.approx(  
        [1.0, 1.0, 1.0], abs=1e-3
    )
