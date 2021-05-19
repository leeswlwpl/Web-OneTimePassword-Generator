# Clientside
import hmac
from hashlib import sha1

KEY = b"randomkeyvaluewleknfifoansf"
counter = 14


def OTP(KEY, counter, n):
    hmac_value = hmac.new(key=KEY, msg=bytes([counter]), digestmod=sha1)
    # print(hmac_value.digest().hex())

    startIndex = int(hmac_value.digest()[19] & 0x0f)
    # print("startIndex = %s"%startIndex)

    hmac_result = hmac_value.digest()[startIndex : startIndex+4]
    # print("hmac_result = %s"%hmac_result.hex())

    hmac_result_masked = int(hmac_result.hex(),16) & int('7fffffff', 16)
    # print("hmac_result_masked = "+str(hmac_result_masked)) # Should be a number at most 10 digits

    OTP_d = pw_digit(hmac_result_masked, n)
    counter+=1

    return OTP_d


def pw_digit(OTP, n): 
    OTP = OTP% pow(10, n)
    while OTP < pow(10, n-1):
        OTP = OTP*10

    return OTP

OTP_6d = OTP(KEY, counter, 6)
print("OTP 6 digits = %s"%OTP_6d)


