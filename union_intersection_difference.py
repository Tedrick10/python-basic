lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "B", "C", "D", "E", "F"}
lettersC = {"G", "H"}

union = lettersA | lettersB
intersection = lettersA & lettersB
anotherIntersection = intersection & lettersC
difference = lettersB - lettersA

print("Union:", "\t\t\t\t\t", union)
print("Intersection:", "\t\t\t", intersection)
print("Another Intersection:", "\t", anotherIntersection)
print("Difference:", "\t\t\t", difference)