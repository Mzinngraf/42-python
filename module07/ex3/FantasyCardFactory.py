import random
from typing import Optional, Union
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    CREATURES = [
        ("Dragon", 5, "Legendary", 7, 5),
        ("Goblin", 2, "Common", 3, 2),
    ]
    SPELLS = [
        ("Fireball", 4, "Rare", "damage"),
        ("Ice Bolt", 2, "Common", "damage"),
        ("Lightning Strike", 3, "Uncommon", "damage"),
    ]
    ARTIFACTS = [
        ("Mana Ring", 2, "Uncommon", 5, "+1 mana per turn"),
        ("Power Staff", 4, "Rare", 3, "+2 attack to all creatures"),
        ("Magic Crystal", 1, "Common", 8, "draw one card per turn"),
    ]

    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        data = random.choice(self.CREATURES)
        name = name_or_power if isinstance(name_or_power, str) else data[0]
        return CreatureCard(name, data[1], data[2], data[3], data[4])

    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        data = random.choice(self.SPELLS)
        name = name_or_power if isinstance(name_or_power, str) else data[0]
        return SpellCard(name, data[1], data[2], data[3])

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        data = random.choice(self.ARTIFACTS)
        name = name_or_power if isinstance(name_or_power, str) else data[0]
        return ArtifactCard(name, data[1], data[2], data[3], data[4])

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        creators = [
            self.create_creature,
            self.create_spell,
            self.create_artifact,
        ]
        for i in range(size):
            cards.append(creators[i % len(creators)]())
        return {"theme": "Fantasy", "cards": cards, "size": len(cards)}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
