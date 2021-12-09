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

    memo[n] = fibonaaci_memoization(n - 1, memo) + fibonaaci_memoization(n - 2, memo)
    return memo[n]


def longest(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])


if __name__ == "__main__":
    # n = int(input())
    # print(fibonaaci(n)
    # print(fibonaaci_memoization(n, [None] * (n + 1)))
    print(longest([2, 3, -2, 4, 5]))
