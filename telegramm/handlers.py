from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, state
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import requests
import telegramm.keyboards as kb
from consts import *

router = Router()


class Register(StatesGroup):
    name = State()
    password = State()
    id_user = State()
    phone_user = State()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAKWQGYwoJnQtmM453xUE46hATztgheOAAKsEwACOJ4hS9HIZVrp3vjbNAQ")
    await message.answer(START_MESSAGE_ANSWER, reply_markup=kb.main)


@router.message(Command("Вход"))
async def cmd_start(message: types.Message):
    await state.set_state(Register.name)
    await message.answer(ANSWER_ABOUT_LOGIN)


@router.message(Register.name)
async def reg_name(messange: Message, state: FSMContext):
    await state.update_data(name=messange.text)
    await state.set_state(Register.password)
    await messange.answer(ANSWER_ABOUT_PASWORD)


@router.message(Register.password)
async def reg_age(messange: Message, state: FSMContext):
    await state.update_data(age=messange.text)
    data = await state.get_data()
    db_session.global_init("db/blogs.db")
    na = data['name']
    ag = data['age']
    user = User()
    user.name = na
    user.hashed_password = ag
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    await messange.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}')
    await state.clear()
