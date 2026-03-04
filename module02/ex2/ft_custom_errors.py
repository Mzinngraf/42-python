class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_status(plant_name):
    if plant_name.lower() == "tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water_tank(level):
    if level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant_status("tomato")
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        check_water_tank(0)
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")
    try:
        check_plant_status("tomato")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_water_tank(0)
    except GardenError as e:
        print("Caught a garden error:", e)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
