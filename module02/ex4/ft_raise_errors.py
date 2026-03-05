def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty")

    if water_level < 1 or water_level > 10:
        raise ValueError("Invalid water level")

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Invalid sunlight hours")

    return "Plant is healthy"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print("Error:", e)

    try:
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print("Error:", e)

    try:
        print(check_plant_health("lettuce", 15, 8))
    except ValueError as e:
        print("Error:", e)

    try:
        print(check_plant_health("carrot", 5, 0))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    test_plant_checks()
