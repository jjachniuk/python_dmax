import requests

api_url = "https://<url of dmax>/"
headers = {
    "apikey": "<apikey>",
    "filename" : "<filename>"
}
with open('2.pdf', 'rb') as f:
    response = requests.post(api_url + "avsanitizesync",headers=headers, data=f)

dataid = response.json()["data_id"]

headers = {
    "apikey": "<apikey>",
    "dataid" : dataid
}

response = requests.get(api_url + "getcleanfile",headers=headers)


if response.status_code == 200:
    with open('<new filename>', 'wb') as f:
        f.write(response.content)
