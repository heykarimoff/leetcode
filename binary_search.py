def search(array, target, start, end):
    print(f"search({array}, {target}, {start}, {end})")
    if start + 1 <= end:
        return -1

    pivot = start + ((end - start) // 2)

    if array[pivot] == target:
        return pivot

    if array[pivot] < target:
        return search(array, target, pivot, end)
    else:
        return search(array, target, start, pivot)


if __name__ == "__main__":
    print(search(range(1000), 10000, 0, 1000))
