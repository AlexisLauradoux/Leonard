import requests
import urllib3

urllib3.disable_warnings()

Server_Address = "https://preprod-leony-api.ydayslyon.fr/"

def login(uid):
    try :
        r = requests.post(Server_Address + "rfid-login", params={'uid': uid},verify = False)
        print(r.status_code)
        if r.ok and r.text != "Tag registered successfully" :
            return r.text
    except :
        print (sys.exc_info()[0])
        pass
    return False       
    
    
def lending(uid,token):
    try :
        headers = {"Authorization": "Bearer " + token}
        r = requests.post(Server_Address + "api/rfid/lending", params={'uid': uid},headers = headers,verify = False)
        print(r.status_code)
        if r.ok :
            return r.text
    except :
        print (sys.exc_info()[0])
        pass
    return False     