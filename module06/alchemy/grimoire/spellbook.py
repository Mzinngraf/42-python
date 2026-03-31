def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell after validating its ingredients.

    Uses a late import of validate_ingredients to avoid any potential
    circular dependency between spellbook and validator.
    """
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if "VALID" in validation_result and "INVALID" not in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
