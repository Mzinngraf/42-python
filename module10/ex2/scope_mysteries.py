from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    # Output baseado no PDF [cite: 174]
    print("Testing mage counter...")
    ca = mage_counter()
    cb = mage_counter()
    print(f"counter_a call 1: {ca()}")
    print(f"counter_a call 2: {ca()}")
    print(f"counter_b call 1: {cb()}")

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    acc_reset = spell_accumulator(100)
    print(f"Base 100, add 30: {acc_reset(30)}")

    print("Testing memory vault...")
    v = memory_vault()
    v['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {v['recall']('secret')}")
    print(f"Recall 'unknown': {v['recall']('unknown')}")
