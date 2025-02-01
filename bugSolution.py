def function_with_uncommon_bug(x):
    if x == 0:
        return 0  # Corrected base case
    else:
        return x * function_with_uncommon_bug(x - 1)

print(function_with_uncommon_bug(5))  # Correct output