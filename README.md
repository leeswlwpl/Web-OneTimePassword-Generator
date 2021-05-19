# Web-OneTimePassword-Generator
## One Time Password Generator
### HMAC-based OTP (RFC 4226)
- Based on hash-based message authentication codes (HMAC)
- Using SHA-1 hash
- Password depends on the secret key (also called the ‘seed’), and a counter. 
- The seed are commonly 160 bits length by default.
- Recommended size of Look-ahead window (valid counter range): +10~15

### Time-based OTP (RFC 6238)
- Modified version of HOTP, and using the time interval as the counter value. 
- Commonly, the counter is the number of 30-second intervals that have elapsed since the Unix time, which is 00:00:00 UTC 1-1-1970.
- e.g. timestamp: “10:27:30 05/11/2020 (UTC)” = 1589236050.
- counter: 1589236050/30 = 52974535
- Recommended size of valid window (valid counter range): +/-5 (2.5 mins before and 2.5 mins after)
