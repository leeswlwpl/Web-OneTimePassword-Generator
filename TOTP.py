# The algorithm of TOTP is similar to HOTP


# The difference is replacing the following codes to change the counter calculation (in both clientside and serverside):
interval = 30
time_elapse = time.time() 
counter = int(time_elapse // interval)


# And change the valid window (in serverside):
counter -= 5
for i in range(0, 11):
    OTP_pw = OTP(KEY, counter, 6)
    if inputCode == OTP_pw:
        print("Succuess authentication!")
        break
        
        
