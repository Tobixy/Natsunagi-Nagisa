import json
import os


def get_user_list(config, key):
    with open("{}/Natsunagi/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

API_ID = 28374181
API_HASH = "00b7ca7f535e816590db39e76f85d0c7"
APP_ID = 28374181
APP_HASH = "00b7ca7f535e816590db39e76f85d0c7"
DB_URL = "mongodb+srv://Shivam10:rLh2OeAtAbtn2L1B@cluster0.m7nxa0j.mongodb.net/?retryWrites=true&w=majority"
TOKEN = "your_bot_token_here"
OWNER_ID = 5715764478
OWNER_USERNAME = "Tobixy"
BOT_USERNAME = "Test_wla_bot"
SUPPORT_CHAT = "botsupportx"
JOIN_LOGGER = -1001952724315
EVENT_LOGS = -1001952724315
ERROR_LOGS = -1001952724315
SQLALCHEMY_DATABASE_URI = "postgres://rrqdvdez:icPxWx-GG7EKxam8H17GVfxC75ZaXxR3@balarama.db.elephantsql.com/rrqdvdez"  # needed for any database modules
MONGO_URI = DB_URL
LOAD = []
NO_LOAD = []
WEBHOOK = False
DEBUG = False
INFOPIC = True
URL = None
SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
MONGO_URI = DB_URL
    

DRAGONS = get_user_list("elevated_users.json", "sudos")
DEV_USERS = get_user_list("elevated_users.json", "devs")
DEMONS = get_user_list("elevated_users.json", "supports")
TIGERS = get_user_list("elevated_users.json", "tigers")
WOLVES = get_user_list("elevated_users.json", "whitelists")
    # Other lists and configurations...
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
    
