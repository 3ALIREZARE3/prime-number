import time
import sys
import matplotlib.pyplot as plt


def generate_primes(limit):
    """
    Generate prime numbers up to the given limit efficiently.

    Args:
    limit (int): The upper bound for generating prime numbers

    Returns:
    tuple: (list of primes, time taken, memory used)
    """
    start_time = time.time()

    # List to store prime numbers
    primes = []

    # Check numbers from 2 to limit
    for num in range(2, limit + 1):
        # Assume the number is prime until proven otherwise
        is_prime = True

        # Only check division by previously found prime numbers
        for prime in primes:
            # If the prime is larger than square root of num, we can stop checking
            if prime * prime > num:
                break

            # If num is divisible by any previous prime, it's not prime
            if num % prime == 0:
                is_prime = False
                break

        # If the number is prime
        if is_prime:
            primes.append(num)

    end_time = time.time()

    # Calculate time and memory
    time_taken = end_time - start_time
    memory_used = sys.getsizeof(primes) / 1024 / 1024  # Convert to MB

    return primes, time_taken, memory_used


def analyze_performance():
    # Test different limits
    limits = [
        10**3,  # Thousand
        10**4,  # Ten Thousand
        10**5,  # Hundred Thousand
        10**6,  # Million
        10**7,  # Ten Million
    ]

    # Lists to store results
    prime_counts = []
    times = []
    memories = []

    # Collect performance data
    for limit in limits:
        primes, time_taken, memory_used = generate_primes(limit)

        prime_counts.append(len(primes))
        times.append(time_taken)
        memories.append(memory_used)

        print(f"Limit: {limit}")
        print(f"Total Primes Found: {len(primes)}")
        print(f"Time Taken: {time_taken:.2f} seconds")
        print(f"Memory Used: {memory_used:.2f} MB\n")

    # Create a figure with two subplots
    plt.figure(figsize=(12, 5))

    # Time Taken Subplot
    plt.subplot(1, 2, 1)
    plt.plot(limits, times, marker="o")
    plt.title("Time Taken vs Limit")
    plt.xlabel("Limit")
    plt.ylabel("Time (seconds)")
    plt.xscale("log")
    plt.grid(True)

    # Memory Used Subplot
    plt.subplot(1, 2, 2)
    plt.plot(limits, memories, marker="o", color="green")
    plt.title("Memory Used vs Limit")
    plt.xlabel("Limit")
    plt.ylabel("Memory (MB)")
    plt.xscale("log")
    plt.grid(True)

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig("prime_performance.png")
    plt.close()

    # Additional visualization for prime count
    plt.figure(figsize=(10, 5))
    plt.plot(limits, prime_counts, marker="o", color="red")
    plt.title("Number of Primes Found vs Limit")
    plt.xlabel("Limit")
    plt.ylabel("Number of Primes")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.savefig("prime_count.png")
    plt.close()


# Run the performance analysis
analyze_performance()

print(
    "Performance graphs have been saved as 'prime_performance.png' and 'prime_count.png'"
)
