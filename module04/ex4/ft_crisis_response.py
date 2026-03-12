def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print("ROUTINE ACCESS: Attempting access to '" + filename + "'...")
    else:
        print("CRISIS ALERT: Attempting access to '" + filename + "'...")

    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            print("SUCCESS: Archive recovered - \"" + content + "\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, fallback protocols engaged")


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

crisis_handler("lost_archive.txt")
crisis_handler("classified_vault.txt")
crisis_handler("standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")