import pandas as pd
import requests
import json

date = "2024-07-07"
url = "https://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=" + str(date)

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

data = requests.get(url, headers=header)
print(data)

js_data = json.loads(data.text)

js_arr= []
for api in js_data["data"]:
    print(api)
    veg_name = str(api["vegetablename"])
    price = str(api["price"])
    retail_price = str(api["retailprice"])
    unit = str(api["units"])
    mall_price = str(api["shopingmallprice"])
    new_js= {
        "date" : str(date),
        "veg_name" : veg_name,
        "price" : price,
        "retail_price" : retail_price,
        "mall_price" : mall_price,
        "unit" : unit,
        }
    js_arr.append(new_js)

df = pd.DataFrame(js_arr)
df.to_csv("Project2.csv")
