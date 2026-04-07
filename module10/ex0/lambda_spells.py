def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get('power', 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    # Output baseado no PDF
    print("Testing artifact sorter...")
    arts = [
        {'name': 'Fire Staff', 'power': 92},
        {'name': 'Crystal Orb', 'power': 85}
    ]
    sorted_arts = artifact_sorter(arts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']} "
          f"({sorted_arts[1]['power']} power)")

    print("Testing spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    print(" ".join(spell_transformer(spells)))
