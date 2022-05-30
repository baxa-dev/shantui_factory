from bot.models import BotUser
from telegram import InlineKeyboardButton
def get_object_or_None(ModelName, id):
    try:
        return ModelName.objects.get(id=id)
    except:
        return None

def get_botuser_object_or_None(id):
    try:
        return BotUser.objects.get(telegram_id=id)
    except:
        return None

def create_inline_buttons(data=None):
    if data:
        keyboard = []
        index = 0
        for item in data:
            menu = False
            if item.get("menu", False) == True:
                menu = True
                keyboard.append([InlineKeyboardButton(item.get('name'), callback_data=item.get('data'))])
            elif item.get("new_line") == True:
                index += 1
            if not menu:
                if index == 0 or item.get("new_line") == True:
                    keyboard.append([InlineKeyboardButton(item.get('name'), callback_data=item.get('data'))])
                else:
                    keyboard[index].append(InlineKeyboardButton(item.get('name'), callback_data=item.get('data')))

        return keyboard
    return [[InlineKeyboardButton("Назад в главное меню", callback_data='home'),]]

data = [
    {'name':"Zavod", "data":"zavod", "new_line":False}
]
