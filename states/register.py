from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    name = State()
    birthdate = State()
    phone = State()
    photo = State()
