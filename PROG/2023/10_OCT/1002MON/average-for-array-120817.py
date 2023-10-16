def solution(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [i+1 for i in range(10)]
    solve = solution(numbers)
    print(solve)