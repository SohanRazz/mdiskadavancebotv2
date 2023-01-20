# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "21948679"))
    API_HASH = os.environ.get("API_HASH", "d1a9ac6ab9cfa0cefc908280c8a3cca1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5839090719:AAGY1G-D4gowK1FtgITSXnTkHOpy-Jqpv2g")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCWSAiGrKYX-jitLVr8_6YinyakxlSZ5NfblrkqPToINU0FZB2V-IObBjNRLnk5I--yuTWhxu172IQDFEdfPvIm7PpoGtqUUd-m6XBinFNxur5zR7CyyUbWdf_cX8AkkemaFyHc3CytYA8ScRx136vov1i-Z0UuLnL0u9UKkWzksMPjNE8udt_2t8rI-uGwnTrZNpSsWoL_BLGrlojUS6MAAS2O4IIuhUQgT89WnMDkjk-9yZM6g7faNlWMGy67NUgTc03UngT8HxmKJr6Z52yADH3Sn7mp4nR4-x3ZDE13AHHkpsE44OqFW_k7VDck7c5l0WpW3H1lgM_QGdJIghXjAAAAAVyYLBYA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001836945914"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Movies_Searcher2_Mdisk_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","5848443926"))
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Sohanrazz:Sohanrazz@cluster0.bjr2jrh.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>❤️ LazyDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

