def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """

    return x == x % 10 * 100 +x // 10 % 10 * 10 +x // 100 or x == x % 10 * 10 + x // 10 + x // 100 or x // 10 == 0