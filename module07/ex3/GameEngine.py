from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self._factory: CardFactory = None
        self._strategy: GameStrategy = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            return {"error": "Engine not configured"}

        creature = self._factory.create_creature()
        spell = self._factory.create_spell()
        artifact = self._factory.create_artifact()
        hand = [creature, spell, artifact]
        self._cards_created += 3

        hand_display = [f"{c.name} ({c.cost})" for c in hand]
        print(f"Hand: [{', '.join(hand_display)}]")

        result = self._strategy.execute_turn(hand, [])
        damage = result.get("actions", {}).get("damage_dealt", 0)
        self._total_damage += damage
        self._turns_simulated += 1

        return result

    def get_engine_status(self) -> dict:
        strategy_name = (
            self._strategy.get_strategy_name() if self._strategy else None
        )
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
        }
