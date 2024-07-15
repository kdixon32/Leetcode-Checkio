def number_length(value: int) -> int:
    if value < 10:
        return 1
    count = 0
    while value != 0:
        value //= 10
        count += 1
    return count