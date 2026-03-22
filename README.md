Copyright (c) 2026 schwastef
This project is released under the MIT LICENSE.

# some_functions
Repository for handing in homework 1 of the "Open Source Energy System Modeling" VU at TU Wien. The repo contains functions for calculating series and parallel impedances as well as transforming the complex RMS vectors of a three-phase system into symmetrical components (zero sequence, positive sequence, negative sequence).

## main.py
This python script contains example calls of the functions implemented in some_functions.py.

## some_functions.py
In this python script four functions are defined.

### calc_series_impedance(z_list): 
Calculates the total impedance of the impedances in z_list. The assumption is that the impedances are connected in series.

Arguments: z_list is a list with (complex) impedances
Returns: (complex) total impedance

Example call: calc_series_impedance([4 + 5j, 1 - 6j])

### calc_parallel_impedance(z_list): 
Calculates the total impedance of the impedances in z_list. The assumption is that the impedances are connected in parallel.

Arguments: z_list is a list with (complex) impedances
Returns: (complex) total impedance

Example call: calc_parallel_impedance([4 + 5j, 1 - 6j])

### transformation(a, b, c):
Transforms the complex RMS vectors a,b,c into symmetrical components (zero sequence, positive sequence, negative sequence).

Arguments: a,b,c are the three complex RMS vectors of a three phase system
Returns: list [zero sequence, positive sequence, negative sequence]

Example call: transformation(1, (-0.5 + np.sqrt(3) / 2 * 1j)**2, -0.5 + np.sqrt(3) / 2 * 1j)

### inverse_transformation(v0, v1, v2):
Transforms the symmetrical components into the three complex RMS vectors of a three phase system.

Arguments: v0,v1,v2 are the zero sequence, positive sequence and negative sequence
Returns: list of the complex RMS vectors (Phase A, Phase B, Phase C)

Example Call: inverse_transformation(0.0, 1.0, 0.0)

## test_some_functions.py
This python script is used by pytest to run the test of the functions defined in "some_functions.py". It contains one test function for each function in "some_functions.py" with multiple assert statements testing multiple cases.