import requests
import csv

# File path where the downloaded files will be saved
file_path = r"E:/Python_Backend_Internship_Assignments/Day4/NSE/NSE_Data"

# File path for the CSV file that contains the list of stock symbols
symbol_file_path = r"E:/Python_Backend_Internship_Assignments/Day4/NSE/StockNames/EQUITY_L.csv"

# Base URL for the NSE API to fetch historical data for equity stocks
NEWAPI_DOMAIN = 'https://www.nseindia.com/api/historical/cm/equity'

# HTTP headers required by the NSE API to emulate a browser request cookies expire after every 5 minutes
headers = {
    'Accept': '*/*',  # Accept any content type
    'Accept-Encoding': 'gzip, deflate, br, zstd',  # Enable response compression
    'Accept-Language': 'en-US,en;q=0.5',  # Language preference
    'Cookie': '#Your Cookie from Browser',  # Placeholder for required cookies
    'Referer': 'https://www.nseindia.com/get-quotes/equity?symbol=20MICRONS',  # Referrer URL to indicate the source of the request
    'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',  # User-Agent client hints for the browser being emulated
    'Sec-CH-UA-Mobile': '?1',  # Indicating mobile device
    'Sec-CH-UA-Platform': '"Android"',  # Platform being used
    'Sec-Fetch-Dest': 'empty',  # Destination of the fetch request
    'Sec-Fetch-Mode': 'cors',  # Cross-Origin Resource Sharing mode
    'Sec-Fetch-Site': 'same-origin',  # Same-origin request
    'Sec-GPC': '1',  # Global Privacy Control header
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',  # User-Agent string to identify the browser
    'X-Requested-With': 'XMLHttpRequest'  # Indicating that the request was made via XMLHttpRequest
}

# Reading the list of stock symbols from the CSV file
with open(symbol_file_path, 'r') as file:
    reader = csv.reader(file)
    symbols = [row[0] for row in reader]  # Extracting the first column (symbol) from each row

# Defining the series, and date range for the historical data query
series = 'EQ'  # Series type (e.g., equity)
from_date = '01-01-2015'  # Start date for data fetching
to_date = '31-12-2015'  # End date for data fetching maximum is 1 year of data

# Loop through each symbol to download the historical data
for symbol in symbols:
    # Construct the URL to fetch the historical data in CSV format
    url = f"{NEWAPI_DOMAIN}?symbol={symbol}&series=[\"{series}\"]&from={from_date}&to={to_date}&csv=true"

    # Send a GET request to the constructed URL
    response = requests.get(url, headers=headers, stream=True)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Extract the filename from the 'Content-Disposition' header if available
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            filename = content_disposition.split("filename=")[-1].strip('\"')
        else:
            filename = "downloaded_file.csv"  # Use a fallback filename if the header is missing

        # Save the downloaded file to the specified file path
        with open(f"{file_path}/{filename}", 'wb') as file:
            # Write the content in chunks to handle large files efficiently
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks
                    file.write(chunk)
        # Print a success message after the file is saved
        print(f"Download successful! File saved as {filename}")
    else:
        # Print an error message if the download failed
        print(f"Failed to download. Status code: {response.status_code}, Error message: {response.text}")
