import functools
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def dec(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            p = kwargs.get('power', args[2] if len(args) > 2 else 0)
            if p >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return dec


def retry_spell(max_attempts: int) -> Callable:
    def dec(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return dec


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    @retry_spell(3)
    def fail(): raise Exception("Waaaaaaagh")
    print(fail())

    print("\nTesting MageGuild...")
    g = MageGuild()
    print(g.validate_mage_name("Merlin"))
    print(g.validate_mage_name("M1"))
    print(g.cast_spell("Lightning", 15))
    print(g.cast_spell("Spark", 5))
