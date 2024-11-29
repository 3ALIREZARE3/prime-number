def generate_primes(limit):
    """
    Generate prime numbers up to the given limit efficiently.

    Args:
    limit (int): The upper bound for generating prime numbers

    Returns:
    list: A list of prime numbers up to the given limit
    """
    # List to store prime numbers
    primes = []

    # Counter for prime number index
    prime_index = 0

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
            # Increment prime index
            prime_index += 1

            # Immediately print the prime number with its index
            print(f"Prime Index {prime_index}: {num}")

            # Add to the list of primes
            primes.append(num)

    return primes


# Example usage
limit = 9999999
print(f"Finding Prime Numbers up to {limit}:\n")
prime_list = generate_primes(limit)

print("\nFull List of Prime Numbers:", prime_list)
print("Total Number of Primes Found:", len(prime_list))
