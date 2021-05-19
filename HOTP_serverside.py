# (Extra) Server-side verification, to verify client's input code 
## To check your output password validation

import hmac
from hashlib import sha1

# Server-side
KEY = b"randomkeyvaluewleknfifoansf"
server_counter = 10  # last vaild counter record
                 # client-side counter: b"14"

print("Input your 6 digit OTP code here (It should be 6 digit number only):")
inputCode = int(input())


def OTP(KEY, server_counter, n):
    hmac_value = hmac.new(key=KEY, msg=bytes([server_counter]), digestmod=sha1)
    startIndex = int(hmac_value.digest()[19] & 0x0f)
    hmac_result = hmac_value.digest()[startIndex : startIndex+4]
    hmac_result_masked = int(hmac_result.hex(),16) & int('7fffffff', 16)
    
    OTP_d = pw_digit(hmac_result_masked, 6)
    print("OTP 6 digits = %s"%OTP_d)
    
    return OTP_d

def pw_digit(OTP, n): 
    OTP = OTP% pow(10, n)
    while OTP < pow(10, n-1):
        OTP = OTP*10
    return OTP


for i in range(0, 10):
    temp_counter = server_counter + i
    print("Attempting counter: %s"%temp_counter)
    OTP_pw = OTP(KEY, temp_counter, 6)
    if inputCode == OTP_pw:
        print("\nSuccuess authentication!")
        server_counter = temp_counter
        print("Updated server_counter: ", server_counter)
        break
    

