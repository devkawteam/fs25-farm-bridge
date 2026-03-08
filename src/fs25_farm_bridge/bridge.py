import os
import requests
import xml.etree.ElementTree as ET

FEED_URL = "http://144.126.158.162:9120/feed/dedicated-server-stats.xml?code=mt3bqE0kBPlcS8Ld"
BASE44_API = os.environ.get("BASE44_API_URL")
BASE44_API_KEY = os.environ.get("BASE44_API_KEY")


def fetch_server_data():
    """Fetch Farming Simulator server state from the XML feed."""

    print("Fetching Farming Simulator server feed...")

    response = requests.get(FEED_URL, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    data = {
        "serverName": root.findtext("Name"),
        "map": root.findtext("Map"),
        "playersOnline": root.findtext("Players"),
        "slots": root.findtext("Slots"),
        "day": root.find("Environment/Day").text if root.find("Environment/Day") is not None else None,
        "month": root.find("Environment/Month").text if root.find("Environment/Month") is not None else None,
        "year": root.find("Environment/Year").text if root.find("Environment/Year") is not None else None,
        "farms": [],
    }

    farms_xml = root.find("Farms")
    if farms_xml is not None:
        for farm in farms_xml.findall("Farm"):
            data["farms"].append({
                "farmId": farm.get("id"),
                "name": farm.findtext("Name"),
                "money": farm.findtext("Money"),
            })

    return data


def send_to_base44(data):
    """Send the parsed server data to the Base44 API."""

    if not BASE44_API:
        raise RuntimeError("BASE44_API_URL is not configured")

    headers = {"Content-Type": "application/json"}
    if BASE44_API_KEY:
        headers["api_key"] = BASE44_API_KEY

    print("Sending data to Base44...")

    response = requests.post(
        BASE44_API,
        json=data,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()

    return response.json()


def main():
    try:
        server_data = fetch_server_data()
        print(server_data)

        if BASE44_API:
            send_to_base44(server_data)
        else:
            print("BASE44_API_URL not configured.")
    except Exception as e:
        print("ERROR:", e)
        raise
