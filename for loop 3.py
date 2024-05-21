# Loop Control Statements (not mandatory for basic understanding)

# continue - Skips to the next iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
  if num % 2 == 0:  # Skip even numbers
    continue
  print(num)  # Print only odd numbers
