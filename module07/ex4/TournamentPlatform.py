from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches: list[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        self._cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            return {"error": "One or both cards not found"}

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True,
        )
        leaderboard = []
        for rank, card in enumerate(sorted_cards, start=1):
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}",
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        if not self._cards:
            avg_rating = 0
        else:
            avg_rating = sum(
                c.calculate_rating() for c in self._cards.values()
            ) // len(self._cards)
        return {
            "total_cards": len(self._cards),
            "matches_played": len(self._matches),
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
