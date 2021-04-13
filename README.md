# Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/krypton-byte/Countdown-API/tree/master)

# How to Use API
```
Endpoint[GET]: /countdown
Parameter:
    day: int   = optional
    month: int = optional
    year: int  = optional
    tz:timezone = optional

Response:
    day: int
    minute: int
    hour: int
    second: int

Endpoint[GET]: /tz
```