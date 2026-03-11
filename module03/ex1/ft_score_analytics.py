import sys

scores = []

for i in range(1, len(sys.argv)):
    scores.append(int(sys.argv[i]))

print("Scores:", scores)

total = sum(scores)
print("Total:", total)

average = total / len(scores)
print("Average:", average)

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Range:", max(scores) - min(scores))
