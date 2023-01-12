import requests
import sys
import os


myfile = sys.argv[1]

print(myfile)

api_url = "<url>"
apikey = "<apikey>"
headers = {
    "apikey": apikey
    "filename" : myfile
}
with open(myfile, 'rb') as f:
    response = requests.post(api_url + "avsanitizesync",headers=headers, data=f)


myrest = response.json()["result"]

#print(myrest)

if myrest > 0:
    print("infected")
    os.remove(myfile)

else:

    dataid = response.json()["data_id"]

    headers = {
        "apikey": apikey,
        "dataid" : dataid
    }

    response = requests.get(api_url + "getcleanfile",headers=headers)


    if response.status_code == 200:
        with open(myfile, 'wb') as f:
            f.write(response.content)
