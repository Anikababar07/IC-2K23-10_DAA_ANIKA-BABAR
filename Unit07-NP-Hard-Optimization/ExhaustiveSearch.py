# Demonstration of Exhaustive Search
# Finding the largest element in a list

numbers = [12, 45, 7, 89, 34, 56]

largest = numbers[0]

# Check every element one by one
for number in numbers:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number:", largest)