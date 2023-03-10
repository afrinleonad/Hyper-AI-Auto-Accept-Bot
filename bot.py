import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Bot started Join our Channel Moviplex",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("New Movies", url="https://t.me/moviplexx"),
      InlineKeyboardButton("New Series", url="https://t.me/moviplexx")
      ],[
      InlineKeyboardButton("Join Now", url="https://t.me/moviplexx")
      ]]
    await message.reply_text(text="**π·π΄π»π»πΎ...β‘\n\nπΈπ°πΌ π° ππΈπΌπΏπ»π΄ ππ΄π»π΄πΆππ°πΌ π°πππΎ ππ΄πππ΄ππ π°π²π²π΄πΏπ π±πΎπ.\nπ΅πΎπ ππΎππ π²π·π°ππ π²ππ΄π°ππ΄ πΎπ½π΄ π±πΎπ... \nππΈπ³π΄πΎ πΎπ½ πΌπ ππΎππππ±π΄ π²π·π°π½π½π΄π»**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} πΉπΎπΈπ½π΄π³ β‘") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("Bot started Join our Channel Moviplex")
pr0fess0r_99.run()
Give feedback
