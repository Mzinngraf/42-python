from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main() -> None:
    print("=== DataDeck Ability System ===")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 4)

    print("EliteCard capabilities:")
    print(f"- Card: {[m for m in dir(Card) if not m.startswith('_')]}")
    methods = [m for m in Combatable.__dict__ if not m.startswith('_')]
    print(f"- Combatable: {methods}")
    print(f"- Magical: {[m for m in dir(Magical) if not m.startswith('_')]}")

    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    res = warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {res}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
