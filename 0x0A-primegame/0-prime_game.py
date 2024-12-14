#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Return a list of prime numbers up to max_n."""
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if is_prime[p]]

def play_game(n):
    """Simulate the game for a given n and return the winner."""
    if n < 2:
        return "Ben"  # If n is 1, Maria cannot make a move

    primes = sieve_of_eratosthenes(n)
    available = [True] * (n + 1)  # Track available numbers
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        # Find the first available prime
        prime_found = False
        for prime in primes:
            if prime > n or not available[prime]:
                continue
            prime_found = True
            # Remove the prime and its multiples
            for multiple in range(prime, n + 1, prime):
                available[multiple] = False
            break

        if not prime_found:
            return "Ben" if turn == 0 else "Maria"  # Current player cannot move

        # Switch turns
        turn = 1 - turn

def isWinner(x, nums):
    """Determine the overall winner after x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
