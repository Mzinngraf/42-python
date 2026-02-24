class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    oak = Plant("Oak", 200, 365)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {len(plants)}")
