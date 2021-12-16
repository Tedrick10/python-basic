numbers = [1, 2, 3, 4, -1, 0]

numbers.sort()
print("Sort:", numbers)

numbers.reverse()
print("Reverse:", numbers)

numbers.append(1000)
print("Length:", len(numbers))

print("In:", 5 in numbers)
print("Not In:", 5 not in numbers)

numbers.remove(1)
print("Remove With Number:", numbers)

numbers.pop()
print("Pop:", numbers)

del numbers[0]
print("Delete With Position:", numbers)

del numbers[0:3]
print("Delete With Position Range:", numbers)

numbers.clear()
print("Clear:", numbers)
