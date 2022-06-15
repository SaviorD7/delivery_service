from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# The ID of GS
SAMPLE_SPREADSHEET_ID = '13gpNC0V-GVSFbwhhspTef7dHwQkx1ZiGIvuaRTniyD0'
# Data range
SAMPLE_RANGE_NAME = 'A2:D100'
# File name with creds
SERVICE_ACCOUNT_FILE = 'credentials.json'



def get_data_from_sheet():
    """
    Get data from Google Sheet

    Return: List of values 
    """
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        

    except HttpError as err:
        print(err)
    values_clear = list(filter(None, values))
    return values_clear


