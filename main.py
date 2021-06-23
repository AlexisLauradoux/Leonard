import RPi.GPIO as GPIO
import led
import request
import time
import rc522

#Test leds
led.blink_red()
led.blink_green()
led.blink_blue()

user_uid = ""
token = ""
last_uid = ""

while True :

    uid = rc522.wait_and_get_uid()
    uid = [str(int) for int in uid]
    uid = "-".join(uid)
    
    if last_uid == uid :
        time.sleep(1)
        last_uid =""
        continue
    
    print("UID : " + uid)
    print("User UID : "+ user_uid)
    print("Token : "+ token)
            
    if user_uid and uid != user_uid and token:
        print("Lending...")
        response = request.lending(uid,token)
        if response != False :
            print("Lending ok")
            led.blink_green()
        else :
            print("Lending faild")
            led.blink_red()    
    else :
        if uid == user_uid and token :
            token = ""
            uidUser = ""
            led.turn_off_blue()
            print("Logout")
        else : 
            response = request.login(uid)
            print("Login...")
            if response != False :
                token = response
                user_uid = uid
                led.blink_green()
                led.turn_on_blue()
                print("Login ok")
            else :
                print("Login failed")
                led.blink_red()
                
    last_uid = uid
GPIO.cleanup()
