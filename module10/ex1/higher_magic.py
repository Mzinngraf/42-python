from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs), spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_if_condition(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_if_condition


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    res = combo("Dragon", 10)
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("Testing power amplifier...")
    p_orig = 10
    mult = 3
    mega_fireball = power_amplifier(fireball, mult)

    print(f"Original: {p_orig}, Amplified: {p_orig * mult}")
