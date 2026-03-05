class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants = []
        self.water_level = 10

    def add_plant(self, name):
        if name == "":
            raise PlantError("Invalid plant name")
        self.plants.append(name)
        print("Added plant:", name)

    def water_plants(self):
        print("Opening watering system")

        try:
            if self.water_level <= 0:
                raise WaterError("No water in tank")

            for plant in self.plants:
                print("Watering", plant)
                self.water_level -= 1

        finally:
            print("Closing watering system")

    def check_health(self, plant, water, sun):
        if plant == "":
            raise ValueError("Invalid plant")

        if water < 1 or water > 10:
            raise ValueError("Invalid water level")

        if sun < 2 or sun > 12:
            raise ValueError("Invalid sunlight")

        print(plant, "is healthy")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print("Error:", e)

    try:
        garden.water_plants()
    except WaterError as e:
        print("Error:", e)

    try:
        garden.check_health("tomato", 5, 8)
        garden.check_health("lettuce", 15, 8)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    test_garden_management()
