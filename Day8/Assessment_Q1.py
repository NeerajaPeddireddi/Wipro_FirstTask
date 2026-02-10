# Write a Python program that:
#
# 1.Uses the requests library to send a GET request to a public REST API(e.g., users or posts API)
#
# 2.Sends custom headers with the request
#
# 3.Parses the JSON response and extracts specific fields
#
# 4.Serializes the extracted data and saves it into a JSON file
#
# 5.Handles HTTP errors using proper exception handling
import json

import requests
get_all_url="https://api.restful-api.dev/objects"
#Custom Headers
headers = {
    "User-Agent": "Python-Requests",
    "Accept": "application/json"
}
try:
    #get request with headers
    get_all_response=requests.get(get_all_url,headers=headers)
    print(headers)
    #raise exception for http errors
    get_all_response.raise_for_status()
    #parse json response
    data=get_all_response.json()
    #Extract specific Fields
    extracted_data=[]
    for item in data:
        extracted_data.append({
            "id":item.get("id"),
            "name":item.get("name"),
        })
    #Saved extracted data to JSON file
    with open("extracted_data.json","w") as f:
        json.dump(extracted_data,f,indent=4)
    print("Extracted Data Saved")
except requests.exceptions.HTTPError as err:
    print("Http Error:",err)
except requests.exceptions.RequestException as err:
    print("Request Error:",err)


