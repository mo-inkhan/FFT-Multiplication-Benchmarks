"""
 * FFT Multiplication Benchmarks
 *
 * @author      Moin Khan
 * @copyright   Moin Khan
 *
 * @link https://mo.inkhan.dev
 *
 */
 """

import timeit
import random
from fft_multiplication import multiply, direct_multiply

def test_direct():
    """
    Direct Multiplication Test

    :returns None
    """

    direct_multiply(p_large, q_large)


def test_fft():
    """
    FFT Multiplication Test

    :returns None
    """
    multiply(p_large, q_large)

degree = 100000

p_large = [random.randint(1, 10) for _ in range(degree)]
q_large = [random.randint(1, 10) for _ in range(degree)]

num_tests = 1
direct_time = timeit.timeit(test_direct, number=num_tests)
fft_time = timeit.timeit(test_fft, number=num_tests)

print(f"FFT multiplication time: {fft_time:.6f} seconds")
print(f"Direct multiplication time: {direct_time:.6f} seconds")
print(f"Performance: {(direct_time-fft_time)/direct_time * 100:.0f} %")
print(f"Degree: {degree}")
print(f"Number of tests: {num_tests}")
