def crisis_handler(filename):
    try:
        if filename == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as file:
            content = file.read().strip()

        print(f'SUCCESS: Archive recovered - "{content}"')
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, failsafe protocols engaged")


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

print("\n")
crisis_handler("ilyas.txt")
print("All crisis scenarios handled successfully. Archives secure.")