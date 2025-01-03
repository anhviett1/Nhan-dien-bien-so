import gspread
from google.oauth2.service_account import Credentials

def save_to_google_sheets(data):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file('path/to/creditentials.json', scopes=SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open('LicensePlates').sheet1
    #sheet.append_row([plate_number])


