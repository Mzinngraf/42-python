from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 6, "wizard_001")

    platform = TournamentPlatform()
    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in [dragon, wizard]:
        stats = card.get_tournament_stats()
        print(f"\n{card.name} (ID: {card.card_id}):")
        print(f"- Interfaces: {stats['interfaces']}")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
