"""
Problem Statement.

    Let's denote a function f(x) in such a way: we add 1 to x, then, while there is
    at least one trailing zero in the resulting number, we remove that zero.
    For example,

        * f(599) = 6: 599 + 1 = 600 → 60 → 6;
        * f(7) = 8: 7 + 1 = 8;
        * f(9) = 1: 9 + 1 = 10 → 1;
        * f(10099) = 101: 10099 + 1 = 10100 → 1010 → 101.

    We say that some number y is reachable from x if we can apply function f to x some
    (possibly zero) times so that we get y as a result. For example, 102 is reachable
    from 10098 because f(f(f(10098))) = f(f(10099)) = f(101) = 102; and any number is
    reachable from itself.

    You are given a number n(1 ≤ n ≤ 10^9); your task is to count how many different
    numbers are reachable from n.

Link: https://codeforces.com/contest/1157/problem/A
"""


def f(x: int):
    """Apply function f to x."""
    return remove_zeros(x + 1)


def remove_zeros(x: int):
    """Remove trailing zeros from a number."""
    return int(str(x).rstrip("0"))


def reachable(n: int):
    """Get all reachable numbers from n."""
    reachable_numbers = [n]
    while True:
        y = f(n)
        if y in reachable_numbers:
            break
        reachable_numbers.append(y)
        n = y

    return reachable_numbers


if __name__ == "__main__":
    n = input("Enter a number: ")
    try:
        n = int(n)
    except ValueError:
        print("Please enter a valid integer.")
        exit(1)
    reachable_numbers = reachable(n)
    print(f"Count: {len(reachable_numbers)}")
    print(f"Reachable numbers: {reachable_numbers}")
