from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    name = State()
    birthdate = State()
    phone = State()
    photo = State()