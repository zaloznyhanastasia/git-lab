def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    return numbers[n//2]
