class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [Rejected]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_info(self) -> str:
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


def main() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print("Initial height:", plant.get_height())
    print("Initial age:", plant.get_age())
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print("Final height:", plant.get_height())
    print("Current plant:", plant.get_info())


if __name__ == "__main__":
    main()
