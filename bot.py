from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackContext,Filters,MessageHandler,CallbackQueryHandler
import json
import os
from likedb import LikeDB
db=LikeDB("db.json")
TOKEN=os.environ.get("TOKEN")
updater=Updater(TOKEN)
dp=updater.dispatcher
def start(update,context):
    chat_id=update.message.chat.id
    bot=context.bot
    like=InlineKeyboardButton(text="👍",callback_data="like")
    dislike=InlineKeyboardButton(text="\U0001F44E",callback_data="dislike")
    keyboard=InlineKeyboardMarkup([
        [like,dislike]
    ],resize_keyboard=True)
    db.save(chat_id)
    bot.sendMessage(chat_id,text="like yoki dislikeni bosing",reply_markup=keyboard)

def sana(update,context):
    query=update.callback_query
    chat_id=query.message.chat.id
    callback_data=query.data
    
    if callback_data=="like":
        db.like(chat_id)
    elif callback_data=="dislike":
        db.dislike(chat_id)
    like=InlineKeyboardButton(text=f"👍 {db.add_like(chat_id)}",callback_data="like")
    dislike=InlineKeyboardButton(text=f"\U0001F44E {db.add_dislike(chat_id)}",callback_data="dislike")
    keyboard = InlineKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)
    text = f"Like or Dislike: {db.add_like(chat_id)}/{db.add_dislike(chat_id)}"
    query.edit_message_text(text, reply_markup=keyboard)



dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(sana))

updater.start_polling()
updater.idle()