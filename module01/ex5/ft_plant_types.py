class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        return self.trunk_diameter * 2

    def get_info(self) -> str:
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (
            f"{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


def main() -> None:
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 50, 40, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1500, 35),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C"),
        Vegetable("Carrot", 30, 60, "spring", "rich in vitamin A"),
    ]

    for f in flowers:
        print(f.get_info())
        f.bloom()

    for t in trees:
        print(t.get_info())
        print(
            f"{t.name} provides "
            f"{t.produce_shade()} square meters of shade"
        )

    for v in vegetables:
        print(v.get_info())
        print(f"{v.name} is {v.nutritional_value}")


if __name__ == "__main__":
    main()
