def logistic_map(r, x):
    return r * x * (1 - x)


def generate_chaotic_numbers(r, x0, n):
    numbers = []
    x = x0
    for _ in range(n):
        x = logistic_map(r, x)
        numbers.append(x)
    return numbers


# Parameters for the logistic map
r = 3.9  # Control parameter
x0 = 0.5  # Initial value

# Generate 100 pseudo-random numbers
numbers = generate_chaotic_numbers(r, x0, 100)

# Print the generated numbers
print("Generated pseudo-random numbers:")
print(numbers)