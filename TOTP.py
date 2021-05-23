# The algorithm of TOTP is similar to HOTP
# The difference is replacing the following codes to change the counter calculation:

interval = 30
time_elapse = time.time() 
interval_count = int(time_elapse // interval)
counter = bytes(interval_count)

