def find_factorial_recursive(number):
    if number == 1:
        return 1
    return find_factorial_recursive(number - 1) * number


def find_factorial_iterative(number):
    result = 1
    while number > 1:
        result = result * number
        number -= 1
    return result


def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    p1, p2 = 0, 1
    for _ in range(n - 2):
        p1, p2 = p2, p1 + p2

    return p1 + p2


# Test
print(fibonacci_iterative(5))
# print(find_factorial_iterative(3))
