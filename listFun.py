

import random

numbers = []
numbers.append(3)
numbers.append(5)
print(numbers)

scores = [62, 56, 78, 91, 82]
print(scores)
print(scores[2])
print(scores.index(91))

print("Min: ", min(scores))
print("Max: ", max(scores))
print("Sum: ", sum(scores))
print()

for i in range(0, 10):
    value = random.random()
    print(i, value)
    
random.shuffle(scores)

print(scores)
