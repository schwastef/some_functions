import numpy as np

f = -0.5 + np.sqrt(3) / 2 * 1j  # 120 degrees rotation operator


def calc_series_impedance(z_list):
    """Calculating the series impedance from the impedances given in z_list."""
    z_ges = 0
    for e in z_list:
        z_ges = z_ges + e
    return z_ges


def calc_parallel_impedance(z_list):
    """Calculating the series impedance from the impedances given in z_list."""
    y_ges = 0
    for e in z_list:
        y_ges = y_ges + 1 / e  # Admittance is used for summation
    return 1 / y_ges  # Impedance is returned


def transformation(a, b, c):
    """Transforming the complex RMS vectors of a three phase system into symmetrical components."""
    v0 = (a + b + c) / 3  # Zero sequence
    v1 = (a + f * b + (f**2) * c) / 3  # Positive sequence
    v2 = (a + (f**2) * b + f * c) / 3  # Negative sequence

    return np.round([v0, v1, v2], 5)


def inverse_transformation(v0, v1, v2):
    """Transforming the symmetrical componets into the complex RMS vectors of a three phase system."""
    a = v0 + v1 + v2  # Complex RMS vector for Phase A
    b = v0 + (f**2) * v1 + f * v2  # Complex RMS vector for Phase B
    c = v0 + f * v1 + (f**2) * v2  # Complex RMS vecotr for Phase C

    return np.round([a, b, c], 5)
