# A number is a perfect square, or a square number, if it is the square of a positive integer. For example, 25 is a square number because 5^2 = 25; it is also an odd square. The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35. Among the first 540 thousand square numbers, what is the sum of all the odd squares?

def oddSquares_540000():
    return sum([i**2 for i in range(1, 540000) if i % 2 == 1])

if __name__ == "__main__":
    print(oddSquares_540000())