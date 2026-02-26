from __future__ import annotations


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        self.total_growth += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def get_display(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_display(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers ({status}), "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    class GardenStats:
        def __init__(self, manager: GardenManager) -> None:
            self._manager = manager

        def plants_added(self, garden_name: str) -> int:
            return len(self._manager._gardens.get(garden_name, []))

        def total_growth(self, garden_name: str) -> int:
            plants = self._manager._gardens.get(garden_name, [])
            return sum(p.total_growth for p in plants)

        def plant_type_counts(self, garden_name: str) -> tuple[int, int, int]:
            plants = self._manager._gardens.get(garden_name, [])
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return (regular, flowering, prize)

    def __init__(self) -> None:
        self._gardens: dict[str, list[Plant]] = {}
        self.stats = GardenManager.GardenStats(self)

    def add_garden(self, garden_name: str) -> None:
        if garden_name not in self._gardens:
            self._gardens[garden_name] = []

    def add_plant(self, garden_name: str, plant: Plant) -> None:
        self.add_garden(garden_name)
        self._gardens[garden_name].append(plant)
        print(f"Added {plant.name} to {garden_name}'s garden")

    def help_all_grow(self, garden_name: str, amount: int = 1) -> None:
        print(f"{garden_name} is helping all plants grow...")
        for p in self._gardens.get(garden_name, []):
            p.grow(amount)

    def report(self, garden_name: str) -> None:
        print(f"=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self._gardens.get(garden_name, []):
            if isinstance(p, (FloweringPlant, PrizeFlower)):
                print(f"- {p.get_display()}")
            else:
                print(f"- {p.name}: {p.height}cm")

        added = self.stats.plants_added(garden_name)
        growth = self.stats.total_growth(garden_name)
        regular, flowering, prize = self.stats.plant_type_counts(garden_name)

        print(f"Plants added: {added}, Total growth: {growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def create_garden_network(cls) -> GardenManager:
        manager = cls()
        manager.add_garden("Alice")
        manager.add_garden("Bob")
        return manager

    def garden_score(self, garden_name: str) -> int:
        score = 0
        for p in self._gardens.get(garden_name, []):
            score += p.height
            if isinstance(p, PrizeFlower):
                score += p.prize_points
        return score

    def gardens_managed(self) -> int:
        return len(self._gardens)


def main() -> None:
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    rose.bloom()
    sunflower.bloom()

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    manager.help_all_grow("Alice", 1)

    manager.report("Alice")

    print(f"Height validation test: {GardenManager.validate_height(-1)}")

    print(
        f"Garden scores - Alice: {manager.garden_score('Alice')}, "
        f"Bob: {manager.garden_score('Bob')}"
    )
    print(f"Total gardens managed: {manager.gardens_managed()}")


if __name__ == "__main__":
    main()
