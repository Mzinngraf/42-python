player1 = {"first_blood", "dragon_slayer", "treasure_hunter"}
player2 = {"first_blood", "arena_master"}
player3 = {"dragon_slayer", "explorer"}

all_achievements = player1 | player2 | player3

print("All achievements:", all_achievements)

common = player1 & player2 & player3
print("Common achievements:", common)

print("Player1 exclusive:", player1 - player2 - player3)