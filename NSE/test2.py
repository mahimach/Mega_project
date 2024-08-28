import requests
import pandas as pd

def download_csv():
    # Define the request URL with the parameters
    url = "https://api.bseindia.com/BseIndiaAPI/api/StockPriceCSVDownload/w"
    params = {
        "pageType": "0",
        "rbType": "D",
        "Scode": "500325",  # Replace with the desired stock code
        "FDates": "01/01/2015",  # Start date
        "TDates": "26/08/2024",  # End date
        "Seg": "C"  # Segment type
    }

    # Define headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.6",
        "Referer": "https://www.bseindia.com/",
        "Upgrade-Insecure-Requests": "1"
    }

    # Send a GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the content to see what is being returned
        print(response.text)  # Check if it's empty or contains an error message

        if response.text.strip() == "":
            print("Received an empty response. Please check the parameters or API endpoint.")
        else:
            # Save the content to a CSV file
            with open(r"C:/Users/dhruv/Downloads/downloaded_file.csv", "wb") as file:
                file.write(response.content)
            print("CSV file downloaded successfully!")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Call the function to download the CSV
download_csv()
