def main():
    try:

        # Step 1 — Download savegame from GPortal
        download_savegame()

        # Step 2 — Fetch server stats XML
        server_data = fetch_server_data()

        # Step 3 — Parse savegame intelligence
        environment = parse_environment()
        farms = parse_farms()
        fields = parse_fields()

        payload = {
            "server": server_data,
            "environment": environment,
            "farms": farms,
            "fields": fields
        }

        print("Payload prepared:")
        print(payload)

        # Step 4 — Send to Base44
        if BASE44_API:
            send_to_base44(payload)
        else:
            print("BASE44_API_URL not configured.")

    except Exception as e:
        print("ERROR:", e)
        raise
