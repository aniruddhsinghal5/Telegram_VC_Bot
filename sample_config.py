HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
    OWNER_ID = int(environ["OWNER_ID"])
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 1794663
    API_HASH = "2dfcf440c50bf255177c79c3a7d7ccf9"
    SUDO_CHAT_ID = -1001299214423
    OWNER_ID = 757533521


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
