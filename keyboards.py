from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

show_r = ReplyKeyboardMarkup(resize_keyboard=True)
show_r.add(KeyboardButton('Показать расписание💜'))

fkne_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('21-КФ', callback_data='21-kf'),
     InlineKeyboardButton('22-КФ', callback_data='22-kf')],
])

half_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Первая', callback_data='first'),
     InlineKeyboardButton('Вторая', callback_data='second')],
])

anoth_w = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Белая',
                          callback_data='Another_Week_White'),
     InlineKeyboardButton('Зелёная',
     callback_data='Another_Week_Green')],
])

anoth_d = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Понедельник',
                          callback_data='Another_Day_pn'),
     InlineKeyboardButton('Вторник',
                          callback_data='Another_Day_vt'),
     InlineKeyboardButton('Среда',
     callback_data='Another_Day_sr')],
    [InlineKeyboardButton('Четверг',
                          callback_data='Another_Day_ct'),
     InlineKeyboardButton('Пятница',
                          callback_data='Another_Day_pt'),
     InlineKeyboardButton('Суббота',
     callback_data='Another_Day_sb')],
])
anoth_show = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Показать', callback_data='a_show')]
])

yest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Вчера',
                          callback_data='Another_Day_Yesterday'),
     InlineKeyboardButton('Завтра',
     callback_data='Another_Day_Tomorday')],
])

all_day_key = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('На университет', callback_data='all_day_uni')],
    [InlineKeyboardButton('На общежитие', callback_data='all_day_ob')]
])

another_key = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Будний день', callback_data='another_day_on')],
    [InlineKeyboardButton('Выходной день', callback_data='another_day_off')]
])

another_route_off_key = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('На университет', callback_data='route_off_uni')],
    [InlineKeyboardButton('На общежитие', callback_data='route_off_ob')]
])

another_route_on_key = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('На университет', callback_data='route_on_uni')],
    [InlineKeyboardButton('На общежитие', callback_data='route_on_ob')]
])