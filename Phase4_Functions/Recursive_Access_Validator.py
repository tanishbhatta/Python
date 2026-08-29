def validate_access_level(num:int) -> int:
    recursive_range = list(range(num, -1, -1))

    return recursive_range

print(validate_access_level(5))