from ex0.Card import Card


class SpellCard(Card):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    def play(self, game_state: dict) -> dict:
        self.used = True
        effect_map = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost} health",
            "buff": "Grant +2/+2 to target creature",
            "debuff": "Reduce target attack by 2",
        }
        effect = effect_map.get(self.effect_type, "Spell effect applied")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
