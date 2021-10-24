def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ArithmeticError("Incorrect value")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n: int, result: int = 1) -> int:
    if n < 0:
        raise ArithmeticError("Incorrect value")
    if n == 1:
        return result

    return factorial_recursive(n - 1, result * n)
