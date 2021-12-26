def fibonaaci(n):
    print(f"fibonaaci({n})")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonaaci(n - 1) + fibonaaci(n - 2)


def fibonaaci_memoization(n, memo):
    print(f"fibonaaci_memoization({n}, {memo})")
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] is not None:
        return memo[n]

    memo[n] = fibonaaci_memoization(n - 1, memo) + fibonaaci_memoization(
        n - 2, memo
    )
    return memo[n]


def test_fibonaaci():
    assert fibonaaci(n=6) == 8


def test_fibonaaci_memoization():
    n = 6
    assert fibonaaci_memoization(n, memo=[None] * (n + 1)) == 8
