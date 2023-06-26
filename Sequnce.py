def main() :
numbers = readFloats(5)
multiply(numbers, 10)
printReversed(numbers)
def readFloats(numberOfInputs) :
print("Enter", numberOfInputs, "numbers:")
inputs = []
for i in range(numberOfInputs) :
value = float(input(""))
inputs.append(value)
return inputs

def multiply(values, factor) :
for i in range(len(values)) :
values[i] = values[i] * factor

def printReversed(values) :
# Traverse the list in reverse order, starting with the last element
i = len(values) - 1
while i >= 0 :
print(values[i], end=" ")
i = i - 1
print()
#enjoy you Start the program now
main()
