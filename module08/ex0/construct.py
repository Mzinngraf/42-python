import sys
import os
import site


def check_matrix_status() -> None:
    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # Unix")
    else:
        venv_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print(f"Package installation path: {site.getsitepackages()[0]}")


if __name__ == "__main__":
    try:
        check_matrix_status()
    except Exception as e:
        print(f"Error: {e}")
