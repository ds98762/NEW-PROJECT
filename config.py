import os
from os import getenv


API_ID = int(getenv("API_ID", "24854614"))
API_HASH = getenv("API_HASH", "bb4a375c908f0681ed4083f4fb3a9ced")
BOT_USERNAME = getenv("BOT_USERNAME", "Rashmika_Robot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6764265589:AAHgdOugeqVu15VmX3USWyRYciqtPKUYIxY")
OWNER_ID = int(getenv("OWNER_ID", "6406965603"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6406965603").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Badmunda_13:badmunda50@cluster0.9oyzqux.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "1BVtsOGUBu0tGskirYQD1QW7Yvx8tufFwRCK2fpIrJwqGGDsnzgm3-Yi-Y4-lr-cuBzovVLjq0Zu2woabaAqSkfwHqCGU5oqhKDhOWh00U_PYv44iM1lyZ1QYgSZRfjCs2B46N9NR6gHChfwRmmdlAOt9oKkySTf3DiQ8-S3AoW5de-4Z8TR1PVd42l-Cs6HiC3_H--aEbdulKTi5ERcshHEK4DhNr0Y_ixfaFz1JyPWx5MLiB8hw2TVz_47MIlyYad3UGlzNAauFr0pApY19P1R33-ny6v2bLN3nszegaH9Le-FA8YsnMGN_kB2cF8K9i1j5GEgwyjVnugi7b-6XAv75GzTzKvo=")
