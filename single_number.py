def single_value_in_arr(arr: list[int]) -> int:
    value = 0
    while True:
        value = arr.pop(0)
        if value not in arr:
            break
        arr.remove(value)
    return value


tests = [
        [1, 2, 3, 4, 3, 2, 1],
        [4, 4, 5, 5, 7, 7, 3],
        [0, 0, 1, 2, 1, 2, 9]
]
if __name__ == '__main__':
    for test in tests:
        print(single_value_in_arr(test))
