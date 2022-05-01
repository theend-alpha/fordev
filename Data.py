from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {} Made by Alpha © 

Do what ya want 

Join group for entertainment!

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("Group", url="https://t.me/BTS_CHAT_ZONE")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [
            InlineKeyboardButton("Owner", url="https://t.me/NotReallyAlpha"),
            InlineKeyboardButton("Group", url="https://t.me/BTS_CHAT_ZONE")
        ],
    ]

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» select pyrogram for music and telethon for rest
» Api id , Api hash , phone number required.
"""

    # About Message
    ABOUT = """
👨‍💻 **About Me** 

Bot to generate session with privacy ! [Alpha](https://t.me/NotReallyAlpha) © 
[Dev](https://t.me/iTz_DEv_xD)
[Alpha](https://t.me/NotReallyAlpha)

Language Used : Python
           
Contact Owner and Developers [here](https://t.me/BTS_CHAT_ZONE) 
"""
