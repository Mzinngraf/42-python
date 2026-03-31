VALID_ELEMENTS = {"fire", "water", "earth", "air"}


def validate_ingredients(ingredients: str) -> str:
    """
    Check whether an ingredient string contains at least one valid element.

    A string is valid if it contains 'fire', 'water', 'earth', or 'air'.
    Returns '[ingredients] - VALID' or '[ingredients] - INVALID'.
    """
    ingredients_lower = ingredients.lower()
    is_valid = any(element in ingredients_lower for element in VALID_ELEMENTS)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
