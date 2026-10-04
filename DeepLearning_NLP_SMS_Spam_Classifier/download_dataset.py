from pathlib import Path
import urllib.request
import zipfile

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

ZIP_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
ZIP_PATH = DATA_DIR / "sms_spam_collection.zip"
RAW_PATH = DATA_DIR / "SMSSpamCollection"

if not RAW_PATH.exists():
    print("Downloading SMS Spam Collection from UCI...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall(DATA_DIR)

    print("Dataset downloaded and extracted.")
else:
    print("Dataset already exists:", RAW_PATH)

if ZIP_PATH.exists():
    ZIP_PATH.unlink()
    print("Removed temporary zip file.")
