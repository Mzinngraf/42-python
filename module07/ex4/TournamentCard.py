from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    BASE_RATING = 1200
    WIN_DELTA = 16
    LOSS_DELTA = 16

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        card_id: str,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = self.BASE_RATING

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Tournament"
        info["attack_power"] = self.attack_power
        info["defense"] = self.defense
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the arena",
        }

    def attack(self, target) -> dict:
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < 10,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += self.WIN_DELTA * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= self.LOSS_DELTA * losses

    def get_rank_info(self) -> dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "card_id": self.card_id,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
        }
