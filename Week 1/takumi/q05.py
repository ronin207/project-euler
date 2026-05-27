# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisible(num):
    return all(num % i == 0 for i in range(1, 21))

if __name__ == "__main__":
    num = 20
    while True:
        if divisible(num):
            print(num)
            break
        num += 20