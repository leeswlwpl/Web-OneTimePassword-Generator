# Clientside
import hmac
from hashlib import sha1

KEY = b"randomkeyvaluewleknfifoansf" # input the secret key
counter = 14


def OTP(KEY, counter, n):
    # For the HMAC value, some people will hash the secret and counter twice, with different padding versions of the secret, 
    # to prevent the length-extension attacks by using different keys on the first and second hashing rounds.
    hmac_value = hmac.new(key=KEY, msg=bytes([counter]), digestmod=sha1)  # using HMAC SHA-1 hash function, the result will be 20 byte long
    
    # For the truncation, we use the last 4 bits of the HMAC value as the index to indicate which 4 bytes we want to truncate to be the result password. 
    # This process is called dynamic truncation. It means that the positions to be truncated are not static , but dependent on the Hash value itself.
    startIndex = int(hmac_value.digest()[19] & 0x0f) # Mask the first 4 bits, only use the last 4 bits as the index for truncation # p.s. 0bxxxx & 0x0f = 0b00xx

    hmac_result = hmac_value.digest()[startIndex : startIndex+4]  # 4 bytes

    # Since some devoce use the most significant bit as signed integers. 
    # To avoid the error caused, we mask it to a 31-bit, unsigned, big-endian integer.
    hmac_result_masked = int(hmac_result.hex(),16) & int('7fffffff', 16) 

    # Finally, output the OTP result to a n-digits number. 
    # In cases of some programs output a different length of password code, for example for 8 digits, we just need to modify the n number:
    OTP_d = pw_digit(hmac_result_masked, n)
    
    # Update the counter value
    counter+=1

    return OTP_d


def pw_digit(OTP, n): 
    OTP = OTP% pow(10, n)
    while OTP < pow(10, n-1):
        OTP = OTP*10

    return OTP

OTP_6d = OTP(KEY, counter, 6)
print("OTP 6 digits = %s"%OTP_6d)


