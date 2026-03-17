import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8593025749:AAEg6vNIquRsDGsSzQgsKFkmxh6M4ETRxCw')
    API_ID = int(os.environ.get("API_ID", '39700479'))
    API_HASH = os.environ.get("API_HASH", 'f013b1c116f9bbf86a3246ffb4a959b8')
    AUTH_USER = os.environ.get('AUTH_USERS', '6934631095').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Son Goku"#Here You Can Change with Your Name  or any custom name or title you prefer
