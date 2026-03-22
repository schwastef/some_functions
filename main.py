# This python script contains example calls of the functions implemented in some_functions.py.

import numpy as np

import some_functions as sf


def main():
    print("Just trying out the functions ...\n")
    a = -0.5 + np.sqrt(3) / 2 * 1j

    print(
        f"Calculate series impedance:\nZ1 = 1 + 3j\nZ2 = 4 + 2j\nZ1 + Z2 = {sf.calc_series_impedance([1 + 3j, 4 + 2j])} Ohm\n"
    )

    print(
        f"Calculate parallel impedance:\nZ1 = 1\nZ2 = 2\nZ3 = 3\nZ4 = 4\nZ1 + Z2 + Z3 + Z4 = {sf.calc_parallel_impedance([1, 2, 3, 4]):.2f} Ohm\n"
    )

    tmp = sf.transformation(1, a**2, a)
    print(
        f"Transforming the complex RMS vectors [Ua, Ub, UC]=[1, e^(j*4*Pi/3), e^(j*2*Pi/3)] to" 
        f"symmetrical components:\nZero sequence: {tmp[0]}\nPositive sequence: {tmp[1]}\nNegative" 
        f"sequence: {tmp[2]}\n"
    )

    tmp = sf.inverse_transformation(0, 1, 0)
    print(
        f"Transforming symmetrical components [V0,V1,V2] = [0,1,0] to complex" 
        f"RMS vectors:\nUa: {tmp[0]}\nUb: {tmp[1]}\nUc: {tmp[2]}\n"
    )


if __name__ == "__main__":
    main()
