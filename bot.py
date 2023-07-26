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
    bot.sendMessage(chat_id,text="Menga rasm yubor!!!")

def sana(update,context):
    query=update.callback_query
    chat_id=query.message.chat.id
    callback_data=query.data
    message_id=query.message.message_id
    if callback_data=="like":
        db.like(message_id,chat_id)
    elif callback_data=="dislike":
        db.dislike(message_id,chat_id)
    like=InlineKeyboardButton(text=f"👍 {db.add_like(message_id,chat_id)}",callback_data="like")
    dislike=InlineKeyboardButton(text=f"\U0001F44E {db.add_dislike(message_id,chat_id)}",callback_data="dislike")
    keyboard = InlineKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)
    text = f"Like or Dislike: {db.add_like(message_id,chat_id)}/{db.add_dislike(message_id,chat_id)}"
    query.edit_message_reply_markup(reply_markup=keyboard)

def photo(update,context):
    bot=context.bot
    query=update.callback_query
    chat_id=update.message.chat.id
    message_id=update.message.message_id
    photo=update.message.photo[-1].file_id
    like=InlineKeyboardButton(text="👍",callback_data="like")
    dislike=InlineKeyboardButton(text="\U0001F44E",callback_data="dislike")
    keyboard=InlineKeyboardMarkup([
        [like,dislike]
    ],resize_keyboard=True)
    db.save(message_id,chat_id)
    bot.sendPhoto(chat_id=chat_id, photo=photo, reply_markup=keyboard)


dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(sana))
dp.add_handler(MessageHandler(Filters.photo,photo))

updater.start_polling()
updater.idle()