FFT Multiplication Benchmarks
=======

Author: **[Moin Khan](https://github.com/mo-inkhan)**

## Introduction

This benchmark compares the performance of FFT and direct multiplication methods for polynomial multiplication across varying degrees, demonstrating the efficiency advantages of FFT for larger input sizes. We will be using the **[fft_multiplication package](https://pypi.org/project/fft-multiplication/)** from PyPI to carry out the tests.

## Benchmarks:

|      | Polynomial 1 Degree | Polynomial 2 Degree | Number of Tests | FFT Multiplication (secs) | Direct Multiplication (secs) | Performance (%) |
| :--- | :------------------ | :------------------ | :-------------- | :------------------------ | :--------------------------- | :-------------- |
| 1    | 1                   | 1                   | 1               | 0.00                      | 0.00                         | -110            |
| 2    | 1                   | 1                   | 10              | 0.00                      | 0.00                         | -167            |
| 3    | 10                  | 10                  | 10              | 0.27                      | 0.00                         | -268846         |
| 4    | 100                 | 100                 | 10              | 0.05                      | 0.00                         | -1591           |
| 5    | 1000                | 1000                | 5               | 0.53                      | 0.42                         | -25             |
| 6    | 5000                | 5000                | 5               | 5.06                      | 10.77                        | 53              |
| 7    | 10000               | 10000               | 5               | 10.6                      | 42.35                        | 75              |
| 8    | 10000               | 10000               | 1               | 0.29                      | 8.47                         | 97              |
| 9    | 50000               | 50000               | 1               | 1.44                      | 211.66                       | 99              |
| 10   | 100000              | 100000              | 1               | 2.88                      | 890.17                       | 100             |


## Summary

The FFT multiplication method excels at efficiently multiplying large polynomials, becoming significantly faster than the direct method as polynomial degrees increase, despite its overhead for smaller input sizes.

1. For very small polynomial degrees (e.g., degrees 1 and 10), the direct multiplication method is faster than the FFT multiplication method, with the performance difference being more pronounced as the number of tests increases This can be attributed to the overhead associated with the FFT algorithm, which outweighs its benefits for small input sizes.
2. As the degrees of the input polynomials increase (e.g., degrees 100 to 1000), the FFT multiplication method starts to show improved performance compared to the direct multiplication method. However, the performance advantage is not consistently significant across all test cases, suggesting that the overhead of the FFT algorithm still plays a role in these cases.
3. For very large polynomial degrees (e.g., degrees 5000 to 100000), the FFT multiplication method consistently outperforms the direct multiplication method, demonstrating its efficiency for large input sizes. The performance improvement is substantial, with the FFT method being up to 100% faster than the direct method.
4. In summary, the FFT multiplication method's performance advantage becomes more apparent as the size of the input polynomials increases. While it may not be the most efficient choice for small input sizes, it is highly effective for large polynomial multiplication problems.

---

## Contributing
All contributions are welcome. Please create an issue first for any feature request
or bug. Then fork the repository, create a branch and make any changes to fix the bug
or add the feature and create a pull request. That's it!
Thanks!

---

## License
**FFT Multiplication Benchmarks** is released under the MIT License.
Check out the full license [here](LICENSE).
