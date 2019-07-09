import requests
import json
import sys

receiver = sys.argv[1]
message = sys.argv[2]

url = "https://chatapi.viber.com/pa/send_message"

payload = {
   "receiver": receiver,
   "min_api_version": 1,
   "sender": {
      "name": "WC DevOps",
      "avatar": "https://media-direct.cdn.viber.com/pg_download?pgtp=icons&dlid=0-04-01-cecbd12d79c81ecc0735fcc2913bc7fe705d15c7d29ec8f7484991fde4e3e91c&fltp=jpg&imsz=0000"
   },
   "tracking_data": "tracking data",
   "type": "text",
   "text": "Deployment is finished: {}".format(message)
}

headers = {
    'Content-Type': "application/json",
    'X-Viber-Auth-Token': "49f3efc15b27d706-c93a2e0b25a905f4-2047e2a0840eb7f1",
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "3fb200a6-7809-4397-8a41-79ba1dfe9918,a4df103b-dfcb-403e-9e07-883381691d84",
    'Host': "chatapi.viber.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "364",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url,
                            data=json.dumps(payload),
                            headers=headers)

print(response.text)
