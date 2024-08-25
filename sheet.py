"""
sheet.py
"""

import logging
import urllib3
import gspread
from oauth2client.service_account import ServiceAccountCredentials


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s"
)

class Sheet():

    def __init__(self, auth, sheet_name, worksheet):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(auth, scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(sheet_name)
        self.log = logging.getLogger(__name__)
        self.worksheet = self.sheet.worksheet(worksheet)
