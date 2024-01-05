from aiogram import types
from aiogram import Dispatcher
from create import bot
from antiflood import rate_limit


@rate_limit(limit=2)
async def ban_user(message: types.Message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    result = await bot.ban_chat_member(chat_id=chat_id, user_id=user_id)

    if result:
        await message.reply("пользователь заблокирован")
    else:
        await message.reply("чето ошибка какаято")


@rate_limit(limit=2)
async def unban_user(message: types.Message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    result = await bot.unban_chat_member(chat_id=chat_id, user_id=user_id)

    if result:
        await message.reply("пользователь разблокирован")
    else:
        await message.reply("чето ошибка какаято")


@rate_limit(limit=2)
async def kick_user(message: types.Message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    result = await bot.kick_chat_member(chat_id=chat_id, user_id=user_id)

    if result:
        await message.reply("пользователь был кикнут")
    else:
        await message.reply("чето ошибка какаято")


def register_ban_kick(dp: Dispatcher):
    dp.register_message_handler(ban_user, commands=['ban'])
    dp.register_message_handler(kick_user, commands=['kick'])
    dp.register_message_handler(unban_user, commands=['unban'])
