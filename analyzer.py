# Анализатор данных 
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    return numbers[n//2]

def read_data(filename):
    with open(filename, 'r') as f:
        return [float(x) for x in f.read().split()]
def format_results(data):
    return f'Результаты: {data}'