## Prime Number Generator and Performance Analyzer

This project implements an efficient algorithm to generate prime numbers up to a specified limit. It also analyzes the performance of the algorithm in terms of execution time and memory usage as the limit increases.

**Features:**

* **Efficient Prime Generation:** The `generate_primes` function uses an optimized approach to find prime numbers by only checking divisibility by previously found primes and utilizing the square root optimization.
* **Performance Analysis:** The `analyze_performance` function tests the prime generation algorithm with different limits and measures the execution time and memory used. 
* **Visualization:** The project generates plots to visualize the performance trends. It includes:
    * **Time Taken vs. Limit:** Shows how execution time increases with the limit.
    * **Memory Used vs. Limit:** Illustrates the relationship between memory consumption and the limit.
    * **Number of Primes Found vs. Limit:** Displays the count of primes generated for each limit.

**How it Works:**

The prime generation algorithm iterates through numbers up to the specified limit. It checks if each number is prime by testing divisibility by previously found primes. If a number is not divisible by any smaller prime, it is considered prime and added to the list. 

The performance analysis function runs the prime generation with increasing limits and records the execution time and memory usage. It then uses Matplotlib to generate plots visualizing the relationship between the limit and performance metrics.

**Usage:**

Simply run the script. It will generate two plots: `prime_performance.png` (showing time and memory) and `prime_count.png` (showing the count of primes). The script will also print the results of the performance analysis to the console.

**Purpose:**

This project serves as a practical example of algorithm efficiency and performance analysis. It demonstrates how to measure and visualize the time and space complexity of an algorithm as the input size grows. This is crucial for understanding how algorithms scale and choosing the best approach for different problem sizes.
