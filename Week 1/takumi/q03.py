# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

def prime_factor(num):
    factors = []
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors

if __name__ == "__main__":
    print(max(prime_factor(600851475143)))