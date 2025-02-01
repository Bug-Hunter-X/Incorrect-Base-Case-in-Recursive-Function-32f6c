def function_with_uncommon_bug(x):
    if x == 0:
        return 1  # Incorrect base case; should be 0
    else:
        return x * function_with_uncommon_bug(x - 1)

print(function_with_uncommon_bug(5))  # Unexpected output due to incorrect base case