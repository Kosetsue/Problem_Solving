def max_digit(value: int) -> int:
    max_num = 0
    nums = str(value)
    split_nums = [int(d) for d in nums]
    max_nums = max(int(*split_nums))

    return max_nums


print("Example:")
print(max_digit(10))
