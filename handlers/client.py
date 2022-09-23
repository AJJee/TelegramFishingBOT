from aiogram import Dispatcher
from aiogram.types import InputMediaPhoto

from create_bot import bot
from keyboards import client_kb
import feed

"""Main functions"""

async def command_hello(message):
    await bot.send_photo(chat_id=message.from_user.id, photo=open('knots/logo.jpg', 'rb'), caption=f'Привіт, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=client_kb.starts)
async def command_start(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_mein.jpg', 'rb') , caption=''), reply_markup=client_kb.kb)

async def knot_pick(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_mein.jpg', 'rb') , caption='Рибацькі вузли'), reply_markup=client_kb.knot)

async def recepy_pick(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_mein.jpg', 'rb') , caption='Рецепти прикормок'), reply_markup=client_kb.recepy)

async def weight(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/weight.jpg', 'rb') , caption='Джигова огрузка під різну глибину'), reply_markup=client_kb.starts)


"""Knot pick functions"""


async def carrot(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/carrot.jpg', 'rb'), caption='Шнур <--->поводок'),reply_markup=client_kb.starts)

async def hook(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/hack.jpg', 'rb'), caption='Карабін<--->поводок'),reply_markup=client_kb.starts)

async def octopus_hook(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/lopatka.jpg', 'rb'), caption='Крючок<--->поводок'),reply_markup=client_kb.starts)

async def swivel(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/vertlug.jpg', 'rb'), caption='Крючок лопатка <---> поводок'),reply_markup=client_kb.starts)

async def carabin(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/carabin.jpg', 'rb'), caption='Вертлюг <--->шнур'),reply_markup=client_kb.starts)


"""Feed functions"""

async def bream(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_feed.jpg', 'rb'), caption=feed.bream), reply_markup=client_kb.starts)

async def crucian_carp(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_feed.jpg', 'rb'), caption=feed.crucian_carp), reply_markup=client_kb.starts)

async def peas(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_feed.jpg', 'rb'), caption=feed.peas), reply_markup=client_kb.starts)

async def roach(message):
    await bot.edit_message_media(chat_id=message.from_user.id, message_id=message.message.message_id, media=InputMediaPhoto(media=open('knots/logo_feed.jpg', 'rb'), caption=feed.roach), reply_markup=client_kb.starts)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_hello, commands=['start'])
    dp.register_callback_query_handler(command_start, text=['/main'])
    dp.register_callback_query_handler(knot_pick, text=['/Рибацькі_вузли'])
    dp.register_callback_query_handler(recepy_pick, text=['/Рецепти_прикормок'])
    dp.register_callback_query_handler(weight, text=['/weight'])

def register_handlers_knots(dp : Dispatcher):
    dp.register_callback_query_handler(carrot, text=['/carrot'])
    dp.register_callback_query_handler(hook, text=['/hook'])
    dp.register_callback_query_handler(octopus_hook, text=['/octopus_hook'])
    dp.register_callback_query_handler(swivel, text=['/swivel'])
    dp.register_callback_query_handler(carabin, text=['/carabin'])

def register_handlers_recepy(dp : Dispatcher):
    dp.register_callback_query_handler(bream, text='/bream')
    dp.register_callback_query_handler(crucian_carp, text='/crucian_carp')
    dp.register_callback_query_handler(peas, text='/peas')
    dp.register_callback_query_handler(roach, text='/roach')

