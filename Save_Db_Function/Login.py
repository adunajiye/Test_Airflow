import json
import requests

def Login():
    sessionid = ""
    payload = {
    "email": "adunajiye@gmail.com",
    "password": "VerdunMason",
    }


    headers = {}
    login_url = "https://vm-backend-ane5.onrender.com/auth/login"
    req = requests.request("POST",login_url, headers=headers, data=json.dumps(payload), verify=False)
    print(req.json)
    # if req.status_code == 200:
    #     response= req.json()
    #     print(response)
    #     sessionid = response['SessionId']
    # return sessionid
Login()