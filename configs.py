# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "29513127"))
    API_HASH = os.environ.get("API_HASH", "bd4ec4de9bb7c3b018ce18a4957e1739")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6255453309:AAG5FVR_pv9km8P40FbVVf1PTn3LtMEMEvk")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQC0dID2Jv9Vc2E6hCgOrrIpsUTDfOyogo2hlNp12fgnhjSDzQKJM2VkeQW2RXUqOpfV5oDROkeyjm88Evx-E63XnhaQszM6njPg87YYTBIXHTs99NCUdkI6rCVtAjgGl6SL_KtTk5GdQ74HTgbYb7SKrNBeBttqlHQcT38ND-cXkSvscog4FPPZ4tzPkaS2gXEs7O9vpmuXipjhSPPeHBGWz0wsvLYQL-8zSQBt-SLG5lzzXV8Ed5fbWOaHj-_M29KDikcDcBp7pjhYEFJ2f7kPOnK6RomaF5jz0FuvjUfKuPeLC12D9tVa09oYLTSPr5UpdCCW8Mww922ER8I1hKBTAAAAAVoyDeoA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001836945914"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Movies_Searcher2_Mdisk_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","5848443926"))
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Sohanrazz:Sohanrazz@cluster0.bjr2jrh.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/Movies_Searcher2_Mdisk_bot'>Movies Searcher Mdisk</a> is an open source project.

    Devs: 
        <a href='https://t.me/Sohan_Rajpurohit_1'>❤️ Sohan_Rajpurohit ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Netflix_Hindi_Movies_4K2'>Movies Searcher Mdisk Bot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/+FVhiCrwL2oJhMGFl'>Support Channel</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/Chat_admin_mdisk_bot'>Sohan_Rajpurohit</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Dear ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/Chat_admin_mdisk_bot'>Sohan_Rajpurohit</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Hunter ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

