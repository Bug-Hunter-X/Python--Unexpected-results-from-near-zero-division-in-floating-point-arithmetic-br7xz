def function_with_uncommon_error(x):
    if x == 0:
        return 0  # This is fine
    elif x > 0:
        return 1 / x  # Potential ZeroDivisionError if x is very small, close to 0
    else:
        return -1

# Example of near-zero input leading to unexpected behavior:
result = function_with_uncommon_error(1e-16) 
print(result) # Output will be huge, and might be unexpected

# Another Example where this could be problematic:
# In machine learning, small values could lead to numerical instability during training.