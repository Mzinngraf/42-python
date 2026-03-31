from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda t: t if isinstance(t, str) else t.get("health", 0),
        )

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_available = 7
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= mana_available - mana_used:
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.cost * 2

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": ["Enemy Player"],
                "damage_dealt": damage_dealt,
            },
        }
