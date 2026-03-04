def garden_operations():
    int("abc")
    _ = 10 / 0
    f = open("missing.txt", "r")
    f.close()
    plants = {"tomato": "healthy"}
    _ = plants["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    try:
        plants = {"tomato": "healthy"}
        _ = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("Testing multiple errors together...")
    try:
        _ = int("abc")
        _ = 1 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error, but program continues! ({type(e).__name__})")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
