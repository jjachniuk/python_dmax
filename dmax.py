import requests

api_url = "https://clouddmax.cybercloudnetworks.net/"
headers = {
    "apikey": "62fa18f7f745406e9320648c1743eebe",
    "filename" : "2.pdf"
}
with open('2.pdf', 'rb') as f:
    response = requests.post(api_url + "avsanitizesync",headers=headers, data=f)

dataid = response.json()["data_id"]

headers = {
    "apikey": "62fa18f7f745406e9320648c1743eebe",
    "dataid" : dataid
}

response = requests.get(api_url + "getcleanfile",headers=headers)


if response.status_code == 200:
    with open('8.pdf', 'wb') as f:
        f.write(response.content)
