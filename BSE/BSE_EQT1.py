import csv
import requests

# File path where the downloaded files will be saved
file_path = r"E:/Python_Backend_Internship_Assignments/Day4/BSE/Downloads/EQT1"

# Constants similar to the ones defined in the Angular app
NEWAPI_DOMAIN = 'https://api.bseindia.com/BseIndiaAPI/api/'
URL_DOWNLOAD_CSV = 'StockPriceCSVDownload/w'  # The correct endpoint

# Custom headers from your devtools, excluding unsupported pseudo-headers
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.6',
    'Referer': 'https://www.bseindia.com/',
    'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    'Sec-CH-UA-Mobile': '?1',
    'Sec-CH-UA-Platform': '"Android"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
}

# Read the CSV file
with open(r"E:\Python_Backend_Internship_Assignments\Day4\BSE\StockNames\EQT1.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        scripcode = row['Security Code']
        pagetype = '0'
        rbType = 'D'  # or 'M' or 'Y'
        monthsFdate = '01/01/2015'  # Example start date
        monthsTdate = '30/06/2024'  # Example end date
        Seg = 'C'

        # Constructing the URL as done in Angular function
        url = f"{NEWAPI_DOMAIN}{URL_DOWNLOAD_CSV}?pageType={pagetype}&rbType={rbType}&Scode={scripcode}&FDates={monthsFdate}&TDates={monthsTdate}&Seg={Seg}"

        # Download the file with stream=True to handle large files
        response = requests.get(url, headers=headers, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Use the 'Content-Disposition' header to extract the filename
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                filename = content_disposition.split("filename=")[-1].strip('\"')
            else:
                filename = f"{scripcode}.csv"  # Fallback filename

            # Save the file to disk
            with open(f"{file_path}/{filename}", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        file.write(chunk)
            print(f"Download successful! File saved as {filename}")
        else:
            print(f"Failed to download. Status code: {response.status_code}, Error message: {response.text}")