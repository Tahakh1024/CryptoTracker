# Cryptocurrency Price Tracker

Welcome to the Cryptocurrency Price Tracker project! This Python script fetches real-time prices of specified cryptocurrencies from the CoinGecko API and logs the data into a Google Sheets document.

## Project Overview

This project is a Cryptocurrency Tracker that fetches real-time prices of specified cryptocurrencies from the CoinGecko API and logs the data into a Google Sheets document. Users can customize the list of cryptocurrencies to track according to their preferences.

## Features

- **Real-Time Data Fetching**: Utilizes the CoinGecko API to fetch current prices of specified cryptocurrencies.
- **Google Sheets Integration**: Logs the fetched data into a Google Sheets document, allowing for easy data visualization and analysis.
- **Scheduled Data Updates**: Automatically updates the Google Sheets document with new cryptocurrency prices at regular intervals using the `schedule` module.

## How to Use

1. **Install Dependencies**: Ensure that you have installed the required Python libraries (`gspread`, `oauth2client`, `requests`, `schedule`) using `pip install -r requirements.txt`.
   
2. **Set Up Google Sheets API**: Due to security concerns, Google Sheets API credentials (JSON key file) are not included in this repository. You can obtain and configure your own credentials following the instructions provided by Google.
   
3. **Run the Script**: Execute the `MainScript.py` script to start fetching and logging cryptocurrency prices to the specified Google Sheets document.
   
4. **Access the Google Sheets Document**: View the logged cryptocurrency price data in the [Google Sheets document](https://docs.google.com/spreadsheets/d/12UUhjGHx5SqHVxwsSu7txmW8TnqDLHP8d5ES9uqNdfI/).

## Note

- **Google Credentials**: This repository does not include Google Sheets API credentials (`cred.json`) due to security reasons. You will need to obtain and configure your own credentials to use the Google Sheets API.
