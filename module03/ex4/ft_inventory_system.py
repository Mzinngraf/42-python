import sys

inventory = {}

for item in sys.argv[1:]:
    name, qty = item.split(":")
    inventory[name] = int(qty)

print(inventory)

total = sum(inventory.values())
print("Total items:", total)

print("Most:", max(inventory, key=inventory.get))
print("Least:", min(inventory, key=inventory.get))