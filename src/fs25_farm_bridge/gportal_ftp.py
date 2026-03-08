import ftplib
import os
from pathlib import Path

FTP_HOST = os.environ.get("GPORTAL_FTP_HOST")
FTP_USER = os.environ.get("GPORTAL_FTP_USER")
FTP_PASS = os.environ.get("GPORTAL_FTP_PASS")

SAVEGAME_DIR = "/profile/savegame1"

LOCAL_SAVEGAME = Path("savegame")
LOCAL_SAVEGAME.mkdir(exist_ok=True)


def download_savegame():
    """Download savegame files from the FS25 server."""

    if not FTP_HOST:
        print("FTP not configured — skipping savegame download")
        return

    print("Connecting to GPortal FTP...")

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    ftp.cwd(SAVEGAME_DIR)

    files = [
        "environment.xml",
        "farms.xml",
        "fields.xml",
        "vehicles.xml",
        "economy.xml"
    ]

    for file in files:
        print("Downloading", file)

        with open(LOCAL_SAVEGAME / file, "wb") as f:
            ftp.retrbinary(f"RETR {file}", f.write)

    ftp.quit()

    print("Savegame download complete.")
