players = [
    {"name": "Alice", "score": 1500},
    {"name": "Bob", "score": 2300},
    {"name": "Charlie", "score": 1800}
]

scores = [p["score"] for p in players]
print(scores)

high = [p for p in players if p["score"] > 1700]
print(high)

score_map = {p["name"]: p["score"] for p in players}
print(score_map)

names = {p["name"] for p in players}
print(names)