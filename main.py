from datetime import datetime
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot_settings.keyboards import fkne_group, half_group, show_r, anoth_w, anoth_d, yest, all_day_key, another_key, \
    another_route_on_key, another_route_off_key
from sql.sqlite_db import db_start, create_profile, update_ring, update_grup, update_half, show_db, show_all, update_frm


proxy_url = 'http://proxy.server:3128'
bot = Bot(token=TOKEN, parse_mode='HTML')  # proxy=proxy_url)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


async def send_message_cron(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=table)


async def send_message_cron0(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t0)


async def send_message_cron1(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t1)


async def send_message_cron2(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t2)


async def send_message_cron3(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t3)


async def send_message_cron4(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t4)


async def send_message_cron5(bot: Bot):
    await db_start()
    records = await show_all()
    for row in records:
        if row[3] == 'on':
            table, t0, t1, t2, t3, t4, t5 = await show_shed(row[0])
            await bot.send_message(chat_id=row[0], text=t5)


async def send_message_interval(bot: Bot):
    await bot.send_message('@onepsuserver', '<em>Бот расписание работает</em>')


async def on_startup(_):
    print('Бот запущен!')
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        send_message_interval,
        trigger='interval',
        hours=1,
        kwargs={
            'bot': bot})
    scheduler.add_job(send_message_cron, trigger='cron', hour=20, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron0, trigger='cron', hour=8, minute=15, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron1, trigger='cron', hour=9, minute=50, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron2, trigger='cron', hour=11, minute=25, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron3, trigger='cron', hour=13, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron4, trigger='cron', hour=14, minute=50, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron5, trigger='cron', hour=16, minute=25, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.start()
    bot_commands = [
        BotCommand(command="/start", description="Выбрать другую группу"),
        BotCommand(
            command="/tram_all",
            description="Посмотреть расписание трамвая на весь день"),
        BotCommand(
            command="/tram_other",
            description="Посмотреть расписание трамвая на другой день"),
        BotCommand(
            command="/other",
            description="Посмотреть расписание на другой день"),
        BotCommand(
            command="/ring_on",
            description="Включить рассылку расписания"),
        BotCommand(
            command="/ring_off",
            description="Выключить рассылку расписания"),
        # BotCommand(command="/zachet", description="Посмотреть расписание зачётов")
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.delete()
    await db_start()
    await create_profile(message.from_user.id)
    await update_frm(message.from_user.id, message.from_user.first_name)
    await bot.send_message(message.from_user.id,
                           '<em>Привет, это <b>бот</b> расписание!</em>')
    await bot.send_message(message.from_user.id,
                           "<em>Выбери группу</em>",
                           reply_markup=fkne_group)


@dp.message_handler(commands=['tram_all'])
async def all_day(message: Message):
    await message.delete()
    await bot.send_message(message.from_user.id,
                           '<em>Расписание на весь день</em>',
                           reply_markup=all_day_key)


@dp.message_handler(commands=['tram_other'])
async def another(message: Message):
    await message.delete()
    await bot.send_message(message.from_user.id,
                           '<em>Выберите день</em>',
                           reply_markup=another_key)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('another_day_'))
async def another_days(callback: types.CallbackQuery):
    if callback.data == 'another_day_on':
        await callback.message.answer('<em>Выберите направление</em>',
                                      reply_markup=another_route_on_key)
    if callback.data == 'another_day_off':
        await callback.message.answer('<em>Выберите направление</em>',
                                      reply_markup=another_route_off_key)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('route_off_'))
async def another_days_route_off(callback: types.CallbackQuery):
    if callback.data == 'route_off_ob':
        await callback.message.answer(f'<em>{ob_off}</em>')
    if callback.data == 'route_off_uni':
        await callback.message.answer(f'<em>{uni_off}</em>')


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('route_on_'))
async def another_days_route_on(callback: types.CallbackQuery):
    if callback.data == 'route_on_ob':
        await callback.message.answer(f'<em>{ob_on}</em>')
    if callback.data == 'route_on_uni':
        await callback.message.answer(f'<em>{uni_on}</em>')


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('all_day_'))
async def another_days(callback: types.CallbackQuery):
    isoWeekDay = datetime.today().isoweekday()
    if callback.data == 'all_day_uni':
        if isoWeekDay <= 5:
            await callback.message.answer(f'<em>{uni_on}</em>')
        elif isoWeekDay >= 6:
            await callback.message.answer(f'<em>{uni_off}</em>')
    if callback.data == 'all_day_ob':
        if isoWeekDay <= 5:
            await callback.message.answer(f'<em>{ob_on}</em>')
        elif isoWeekDay >= 6:
            await callback.message.answer(f'<em>{ob_off}</em>')


@dp.message_handler(commands=['ring_on'])
async def ring_on(message: Message):
    await message.delete()
    ring = 'on'
    await update_ring(message.from_user.id, ring)
    await message.answer(f'<em>Рассылка расписание включена</em>')


@dp.message_handler(commands=['ring_off'])
async def ring_off(message: Message):
    await message.delete()
    ring = 'off'
    await update_ring(message.from_user.id, ring)
    await message.answer(f'<em>Рассылка расписание выключена</em>')


@dp.callback_query_handler(text='21-kf')
async def login_21_kf(callback: types.CallbackQuery):
    await callback.message.delete()
    await update_grup(callback.from_user.id, '21_kf')
    await callback.message.answer("<em>Выбери подгруппу</em>",
                                  reply_markup=half_group)


@dp.callback_query_handler(text='22-kf')
async def login_22_kf(callback: types.CallbackQuery):
    await callback.message.delete()
    await update_grup(callback.from_user.id, '22_kf')
    await callback.message.answer("<em>Выбери подгруппу</em>",
                                  reply_markup=half_group)


@dp.callback_query_handler(text='first')
async def fpl(callback: types.CallbackQuery):
    await callback.message.delete()
    await update_half(callback.from_user.id, 'f')
    await callback.message.answer("<em>Чтобы получить своё расписание нажмите кнопку ниже</em>", reply_markup=show_r)


@dp.callback_query_handler(text='second')
async def spl(callback: types.CallbackQuery):
    await callback.message.delete()
    await update_half(callback.from_user.id, 's')
    await callback.message.answer("<em>Чтобы получить своё расписание нажмите кнопку ниже</em>", reply_markup=show_r)


@dp.message_handler(commands=['other'])
async def another_command(message: types.Message):
    await message.delete()
    await message.answer('<em>Выберите неделю</em>',
                         parse_mode="HTML",
                         reply_markup=anoth_w)


@dp.callback_query_handler(lambda callback_query:
                           callback_query.data.startswith('Another_Week_'))
async def another_week(callback: types.CallbackQuery):
    global a_week
    await callback.message.delete()
    if callback.data == 'Another_Week_Green':
        a_week = 'Green'
    elif callback.data == 'Another_Week_White':
        a_week = 'White'
    await callback.message.answer("<em>Выбери день недели</em>",
                                  parse_mode="HTML",
                                  reply_markup=anoth_d)


@dp.message_handler(Text(equals='Показать расписание💜'))
async def show_rasp(message: types.Message):
    global timetable_today, timetable_today_0, timetable_today_1, timetable_today_2, timetable_today_3, timetable_today_4, timetable_today_5
    await db_start()
    isoWeekDay = datetime.today().isoweekday()
    # if datetime.utcnow().hour >= 17:
    if datetime.now().hour >= 17:
        isoWeekDay = isoWeekDay + 1
    if isoWeekDay >= 7:
        week_count = datetime.today().isocalendar().week - datetime(2022,
                                                                    9, 1, 0, 0, 0).isocalendar().week + 2
        isoWeekDay = 1
    else:
        week_count = datetime.today().isocalendar().week - datetime(2022,
                                                                    9, 1, 0, 0, 0).isocalendar().week + 1
    if week_count % 2 == 0:
        week_today = 'Green'
    else:
        week_today = 'White'
    data_students = await show_db(message.from_user.id)


@dp.message_handler(content_types=['text'])
async def delete_message(message):
    await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
