# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Natsunagi/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    APP_ID = 8172
    APP_HASH ="KNTL"
    DB_URL = "JQUE"
    TOKEN = "BOT_TOKEN"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 945137470  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "FurryChemistry"
    BOT_USERNAME = "NatsunagiProBot"
    SUPPORT_CHAT = "NatsunagiCorporationGroup"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001748076180
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001748076180
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
         -1001657496255
    )
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    MONGO_URI = "mongodb+srv://Shivam10:rLh2OeAtAbtn2L1B@cluster0.m7nxa0j.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    DEBUG = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    MONGO_URI = "KNTL"
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    REDIS_URL = "KNTL"
    BOT_ID = 7373
    ARQ_API_URL = "https://thearq.tech/"
    ARQ_API_KEY = "BCYKVF-KYQWFM-JCMORU-RZWOFQ-ARQ"
    BOT_NAME = "Natsunagi Nagisa"
    BOT_API_URL = "https://api.telegram.org/bot"
    MONGO_DB = "Natsunagi"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
