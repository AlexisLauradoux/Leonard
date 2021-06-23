from pirc522 import RFID
rc522 = RFID()

def wait_and_get_uid():
    while True :
        rc522.wait_for_tag()
        (error, tag_type) = rc522.request()
        
        if not error :
            (error, uid) = rc522.anticoll()
            
            if not error :
                return uid