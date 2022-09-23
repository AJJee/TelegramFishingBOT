from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


btn_start = InlineKeyboardButton(text='Головне меню', callback_data='/main')

kb = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='Рибацькі вузли', callback_data='/Рибацькі_вузли')
b2 = InlineKeyboardButton(text='Рецепти прикормок', callback_data='/Рецепти_прикормок')
b3 = InlineKeyboardButton(text='Джигова огрузка під різну глибину', callback_data='/weight')
kb.add(b1).add(b2).add(b3)

knot = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Шнур <--->поводок', callback_data='/carrot')
btn2 = InlineKeyboardButton(text='Карабін<--->поводок', callback_data='/carabin')
btn3 = InlineKeyboardButton(text='Крючок<--->поводок', callback_data='/hook')
btn4 = InlineKeyboardButton(text='Крючок лопатка <---> поводок', callback_data='/octopus_hook')
btn5 = InlineKeyboardButton(text='Вертлюг <--->шнур', callback_data='/swivel')
knot.add(btn1).add(btn2).add(btn3).add(btn4).add(btn5).add(btn_start)

recepy = InlineKeyboardMarkup(row_width=1)
r_btn1 = InlineKeyboardButton(text='Прикормка на ляща', callback_data='/bream')
r_btn2 = InlineKeyboardButton(text='Прикормка на карася', callback_data='/crucian_carp')
r_btn3 = InlineKeyboardButton(text='Прикормка на плотву', callback_data='/roach')
r_btn4 = InlineKeyboardButton(text='Мастирка горохова', callback_data='/peas')
recepy.add(r_btn1).add(r_btn2).add(r_btn3).add(r_btn4).add(btn_start)

starts = InlineKeyboardMarkup(row_width=1)
starts.add(btn_start)