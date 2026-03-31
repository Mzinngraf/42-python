from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Common", 5,
                               "+1 mana per turn"))

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")

    deck.shuffle()

    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type = type(card).__name__.replace("Card", "")
            print(f"\nDrew: {card.name} ({card_type})")
            print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action: Same interface, different card"
          "behaviors!")


if __name__ == "__main__":
    main()
