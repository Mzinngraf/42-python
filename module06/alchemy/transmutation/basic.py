from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead into gold using fire."""
    fire_result = create_fire()
    return f"Lead transmuted to gold using {fire_result}"


def stone_to_gem() -> str:
    """Transmute stone into a gem using earth."""
    earth_result = create_earth()
    return f"Stone transmuted to gem using {earth_result}"
