import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {"add": operator.add, "multiply": operator.mul,
           "max": max, "min": min}
    return functools.reduce(ops[operation], spells)


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatcher(spell: Any):
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell):
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"
    return dispatcher


if __name__ == "__main__":
    # Output baseado no PDF [cite: 184]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 40, 20], 'max')}")

    print("Testing memoized fibonacci...")
    for i in [0, 1, 10, 15]:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    print("Testing spell dispatcher...")
    d = spell_dispatcher()
    print(d(42))
    print(d("fireball"))
    print(d([1, 2, 3]))
    print(d(None))
