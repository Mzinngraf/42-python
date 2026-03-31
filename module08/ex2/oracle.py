import os
from dotenv import load_dotenv


def connect_to_mainframe() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "unknown")
    api_key = os.getenv("API_KEY")

    print("ORACLE STATUS: Reading the Matrix...")
    if not api_key:
        print("WARNING: API_KEY not found! Access denied.")
        return

    print(f"Configuration loaded:\nMode: {mode}")
    status = "Online" if os.getenv("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {status}")


if __name__ == "__main__":
    connect_to_mainframe()
