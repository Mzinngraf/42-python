def water_plants(plant_list):
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Invalid plant")
            print("Watering", plant)
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Closing watering system")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrot"])

    print("Testing with error...")
    water_plants(["tomato", None, "carrot"])

    print("Cleanup always happens")


if __name__ == "__main__":
    test_watering_system()
