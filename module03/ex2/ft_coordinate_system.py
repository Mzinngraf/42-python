import math

point1 = (0, 0, 0)
point2 = (3, 4, 0)

distance = math.sqrt(
    (point2[0] - point1[0]) ** 2 +
    (point2[1] - point1[1]) ** 2 +
    (point2[2] - point1[2]) ** 2
)

print("Distance:", distance)

coord = "10,20,30"
x, y, z = coord.split(",")

x = int(x)
y = int(y)
z = int(z)

print("Parsed:", (x, y, z))
