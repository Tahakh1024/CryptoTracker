import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import schedule
import time

# Define the scope and credentials for Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheets document by its title
sheet = client.open('Crypto').sheet1

#function to fetch cryptocurrency prices from CoinGecko API
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,binancecoin,Solana,bitcoin-cash', 
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Failed to retrieve data from CoinGecko API: {err}")
        return None

#function to update Google Sheets with cryptocurrency prices
def update_google_sheets():
    data = get_crypto_prices()
    if data:
        # Write headers
        sheet.update_cell(1, 1, 'Cryptocurrency Name')
        sheet.update_cell(1, 2, 'Price')
        sheet.update_cell(1, 3, 'Timestamp')

        # Write data for each cryptocurrency
        row = 2
        for crypto_id, prices in data.items():
            sheet.update_cell(row, 1, crypto_id.capitalize()) #  cryptocurrency name
            sheet.update_cell(row, 2, prices['usd']) # price in USD
            sheet.update_cell(row, 3, '=NOW()') # timestamp
            row += 1

# Schedule the function to update Google Sheets with cryptocurrency prices every 1 minutes
schedule.every(1).minutes.do(update_google_sheets)

while True:
    schedule.run_pending()
    time.sleep(1)

# To manually trigger the data update, call the function update_google_sheets().
# Following line can be uncommented to run the function once when the script starts.
# update_google_sheets()
