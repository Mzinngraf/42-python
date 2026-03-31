from .basic import lead_to_gold

from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the philosopher's stone from gold and a healing potion."""
    gold_result = lead_to_gold()
    healing_result = healing_potion()
    return (
        f"Philosopher's stone created using {gold_result}"
        f" and {healing_result}"
    )


def elixir_of_life() -> str:
    """Create the elixir of life."""
    return "Elixir of life: eternal youth achieved!"
