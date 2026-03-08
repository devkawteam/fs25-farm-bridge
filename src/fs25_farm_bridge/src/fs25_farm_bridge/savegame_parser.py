import xml.etree.ElementTree as ET
from pathlib import Path


SAVEGAME_PATH = Path("savegame")


def parse_environment():
    file = SAVEGAME_PATH / "environment.xml"
    if not file.exists():
        return {}

    root = ET.parse(file).getroot()

    return {
        "day": root.findtext("day"),
        "month": root.findtext("month"),
        "year": root.findtext("year"),
    }


def parse_farms():
    file = SAVEGAME_PATH / "farms.xml"
    if not file.exists():
        return []

    root = ET.parse(file).getroot()

    farms = []

    for farm in root.findall("farm"):
        farms.append({
            "farmId": farm.get("farmId"),
            "name": farm.findtext("name"),
            "money": farm.findtext("money"),
        })

    return farms


def parse_fields():
    file = SAVEGAME_PATH / "fields.xml"
    if not file.exists():
        return []

    root = ET.parse(file).getroot()

    fields = []

    for field in root.findall("field"):
        fields.append({
            "fieldId": field.get("fieldId"),
            "cropType": field.findtext("fruitType"),
            "growthState": field.findtext("growthState"),
            "fertilized": field.findtext("fertilizerState"),
        })

    return fields
