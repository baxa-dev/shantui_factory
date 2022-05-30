from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import InlineKeyboardMarkup, KeyboardButton, Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext
from telegram.utils.request import Request
from bot.management.commands.utils import get_botuser_object_or_None, create_inline_buttons
from bot.models import BotUser
from core.models import Factory, FactoryApplication, ServiceCenterRequest, SpecialTechnique, \
    SpecialTechniqueApplication, SpecialTechniqueCategory

group_username = '@ShantuiReferencesChannel'

echo_field = dict()
users = dict()


def start(update: Update, context: CallbackContext) -> None:
    global echo_field
    user_id = update.message.from_user.id
    print(user_id)
    user = get_botuser_object_or_None(user_id)
    if user != None:
        keyboard = create_inline_buttons([
            {'name': "Спец Техника 🚜", "data": "special-technique-category", "new_line": False},
            {'name': "Заводы 🏗", "data": "factories", "new_line": True},
            {'name': "Сервис Центр 🔧", "data": "service-center", "new_line": False},
            {'name': "Наш каталог 📒", "data": "catalog", "new_line": True},
            {'name': "О нас 🛡", "data": "about", "new_line": False},
        ])
        update.message.reply_html(f'<b>Главное меню</b>', reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        echo_field[f"{user_id}"] = "first_name"
        update.message.reply_html(text="Введите имя")


def echo(update: Update, context: CallbackContext) -> None:
    global echo_field, users
    msg = update.message.text
    user_id = update.message.chat_id
    print(user_id)
    e_field = echo_field.get(f"{user_id}")
    if e_field == "first_name":
        user = BotUser(telegram_id=user_id, first_name=msg)
        users[f'{user_id}'] = user
        echo_field[f"{user_id}"] = "last_name"
        update.message.reply_text("Введите фамилию")
    elif e_field == "last_name":
        users[f'{user_id}'].last_name = msg

        reply_markup = ReplyKeyboardMarkup([[KeyboardButton('Поделиться контактом', request_contact=True)]],
                                           resize_keyboard=True)
        echo_field[f"{user_id}"] = "phone"
        update.message.reply_text('Введите свой номер телефона', reply_markup=reply_markup)
    elif e_field == "phone":
        reply_markup = ReplyKeyboardMarkup([[KeyboardButton('Поделиться контактом', request_contact=True)]],
                                           resize_keyboard=True)

        update.message.reply_text('Введите свой номер телефона ', reply_markup=reply_markup)
    else:
        update.message.reply_text(update.message.text)


def inline_buttons(update: Update, context: CallbackContext) -> None:
    global group_username
    query = update.callback_query
    user_id = query.from_user.id
    user = get_botuser_object_or_None(id=user_id)
    if user == None:
        start(update, context)
    if query.data == "plus":
        obj = ServiceCenterRequest.objects.create(user=user)
        query.answer(text=f'Спасибо, что поинтересовались! ✅', show_alert=True)
        context.bot.send_message(chat_id=group_username, parse_mode="html",
                                 text='<b>{}</b>\n<b>👤Имя:</b> {}\n<b>📞Номер телефона:</b> {} '.format(
                                     'Сервис Центр 🔧', user.get_full_name, user.phone_number))


    elif query.data.split('/')[0] in ('rst', 'rf'):
        id = int(query.data.split('/')[1])
        if query.data.split('/')[0] == 'rst':
            object = SpecialTechnique.objects.get(id=id)
            obj = SpecialTechniqueApplication.objects.create(specialTechnique=object, user=user)
            context.bot.send_message(chat_id=group_username, parse_mode="html",
                                     text='<b>Спец Техники 🚜</b>\n<b>{}</b>:{}\n<b>👤Имя:</b> {}\n<b>📞Номер телефона:</b> {} '
                                     .format(object.category.name, object.name, user.get_full_name, user.phone_number))

            query.answer(text=f'{object} ✅', show_alert=True)
        else:
            object = Factory.objects.get(id=id)
            obj = FactoryApplication.objects.create(factory=object, user=user)
            context.bot.send_message(chat_id=group_username, parse_mode="html",
                                     text='<b>Заводы 🏗</b>\n<b>{}</b>\n<b>👤Имя:</b> {}\n<b>📞Номер телефона:</b> {} '
                                     .format(object.name, user.get_full_name, user.phone_number))
            query.answer(text=f'{object} ✅', show_alert=True)
    else:
        query.answer()
        query.delete_message()
    if query.data == "home":
        keyboard = create_inline_buttons([
            {'name': "Спец Техники 🚜", "data": "special-technique-category", "new_line": False},
            {'name': "Заводы 🏗", "data": "factories", "new_line": True},
            {'name': "Сервис Центр 🔧", "data": "service-center", "new_line": False},
            {'name': "Наш каталог 📒", "data": "catalog", "new_line": True},
            {'name': "О нас 🛡", "data": "about", "new_line": False},
        ])
        query.message.reply_html("Главное меню", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "special-technique-category":
        special_texnique_category = SpecialTechniqueCategory.objects.all()
        keyboard = []
        for i in range(1, len(special_texnique_category) + 1, 1):
            print()
            if i % 2 == 0 and i != 0:
                keyboard.append({'name': special_texnique_category[i - 1].name,
                                 "data": "stc/" + str(special_texnique_category[i - 1].id), "new_line": True})
            else:
                keyboard.append({'name': special_texnique_category[i - 1].name,
                                 "data": "stc/" + str(special_texnique_category[i - 1].id), "new_line": False})
        keyboard.append({'name': "Назад в главное меню", "data": 'home', "new_line": True})
        query.message.reply_html("Специальные техники 🚜",
                                 reply_markup=InlineKeyboardMarkup(create_inline_buttons(keyboard)))
    elif query.data == "factories":
        factory = Factory.objects.all()
        keyboard = []
        for i in range(1, len(factory) + 1, 1):
            if i % 2 == 0 and i != 0:
                keyboard.append({'name': factory[i - 1].name, "data": "f/" + str(factory[i - 1].id), "new_line": True})
            else:
                keyboard.append({'name': factory[i - 1].name, "data": "f/" + str(factory[i - 1].id), "new_line": False})

        keyboard.append({'name': "Назад в главное меню", "data": 'home', "new_line": True})
        query.message.reply_html("Заводы 🏗", reply_markup=InlineKeyboardMarkup(create_inline_buttons(keyboard)))
    elif query.data == "about":
        about_text = """Компания СП ООО "<b>SPETS TEXNIKA TASHKENT</b>" (Спецтехника Ташкент) - имеет <b>17</b> летний опыт в сфере поставок спецтехники и оборудования из Китая. 🚜\nМы работаем только с проверенными крупнейшими заводами Китая, производственная мощь которых составляет не менее 1000 единиц производимой продукции в месяц. Мы заботимся о Вашем бизнесе и своей репутации🛡\n\nSTT - ваш надежный поставщик спецтехники из Китая 🇨🇳🇺🇿\n\nНаши соц.сети\n<a href="https://t.me/sttuzb">Telegram</a>\n<a href="https://vm.tiktok.com/ZSJHXhsCm/">TikTok</a>\n<a href="https://www.youtube.com/channel/UCbVYAfWBA78oYYu3ei4OWcA/videos">Youtube</a>\n<a href="https://www.facebook.com/sttuzb">Facebook</a>\n<a href="https://www.instagram.com/stt_uz/">Instagram</a>"""
        keyboard = create_inline_buttons([{'name': "Назад в главное меню", "data": 'home', "new_line": True}])
        query.message.reply_html(text=about_text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "service-center":
        keyboard = create_inline_buttons([
            {'name': "➕ Оставить заявку", "data": 'plus', "new_line": True},
            {'name': "Назад в главное меню", "data": 'home', "new_line": True}
        ])
        information = "Компания СП ООО «<b>SPETS TEXNIKA TASHKENT</b>» имеет многолетний опыт в поставке спецтехники." \
                      "\nТакже у нас есть два вида сервисного обслуживания, так как только наша компания даёт <b>1,5</b> года гарантию на технику." \
                      "\nМы заботимся о вашем бизнесе и своей репутации!" \
                      "\n    <b>1</b>.	Мобильное сервисное обслуживание всего гарантийного периода. Наши профессиональные специалисты с многолетним опытом и стажем приедут к вам на своих авто, установят причину и также устранят её в самые короткие сроки." \
                      "\n    <b>2</b>.	Сервисное обслуживание на платной основе. \nТакже наши опытные механики могут выехать к вам и разобраться в проблеме на определённых условиях." \
                      "\nМы уверены в своей техники. А также будем рады Вам помочь!"
        query.message.reply_html(text=information, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "catalog":
        keyboard = create_inline_buttons([
            {'name': "Назад в главное меню", "data": 'home', "new_line": True}
        ])
        file = open(str(settings.MEDIA_ROOT) + "/catalog.pdf", 'rb')
        query.message.reply_document(document=file, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data.split('/')[0] == 'f':
        id = int(query.data.split('/')[1])
        object = Factory.objects.get(id=id)
        image = open(str(settings.MEDIA_ROOT) + "/" + str(object.image), 'rb')
        keyboard = create_inline_buttons([
            {'name': "➕ оставить заявку", "data": f'rf/{id}', "new_line": False},
            {'name': "Назад в главное меню", "data": 'home', "new_line": False},
        ])
        query.message.reply_photo(photo=image, caption=f"<b>{object.name}</b>\n{object.description_bot}", parse_mode="HTML",
                                  reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data.split('/')[0] == "stc":
        id = int(query.data.split('/')[1])
        category = SpecialTechniqueCategory.objects.get(id=id)
        special_texniques = SpecialTechnique.objects.filter(category=category)
        keyboard = []
        for i in range(len(special_texniques)):

            last_id = special_texniques.last().id
            print(last_id, special_texniques[i].id)
            if i % 2 == 0 and i != 0:
                keyboard.append(
                    {'name': special_texniques[i].name, "data": "st/" + str(id) + "/" + str(special_texniques[i].id),
                     "new_line": True})
            else:
                new_line = False
                if special_texniques[i].id == last_id:
                    new_line = True
                keyboard.append(
                    {'name': special_texniques[i].name, "data": "st/" + str(id) + "/" + str(special_texniques[i].id),
                     "new_line": new_line})

        keyboard.append({'name': "Назад в главное меню", "data": 'home', "new_line": False, "menu": True})
        keyboard.append({'name': "Назад", "data": 'special-technique-category', "new_line": False, "menu": True})

        query.message.reply_html(f"{category.name}", reply_markup=InlineKeyboardMarkup(create_inline_buttons(keyboard)))

    elif query.data.split('/')[0] == 'st':
        keyboard = []
        id = int(query.data.split('/')[2])
        object = SpecialTechnique.objects.get(id=id)
        image = open(str(settings.MEDIA_ROOT) + "/" + str(object.image), 'rb')

        keyboard.append({'name': "➕ оставить заявку", "data": f'rst/{id}', "new_line": False})
        keyboard.append({'name': "Назад в главное меню", "data": 'home', "new_line": False})
        keyboard.append({'name': "Назад Спец Техники", "data": 'special-technique-category', "new_line": True})
        keyboard.append({'name': "Назад", "data": 'stc/' + query.data.split('/')[1], "new_line": False})
        text = f"\n\n{object.description_bot}" if object.description_bot else ""
        query.message.reply_photo(photo=image, caption=f"<b>{object.name}</b>{text}", parse_mode="HTML", reply_markup=InlineKeyboardMarkup(create_inline_buttons(keyboard)))


def registerContact(update: Update, context: CallbackContext) -> None:
    global echo_field, users
    user_id = update.message.from_user.id
    e_field = echo_field.get(f"{user_id}")
    if e_field == "phone":
        users[f'{user_id}'].phone_number = update.message.contact.phone_number
        echo_field[f'{user_id}'] = None
        users[f'{user_id}'].save()
        del echo_field[f'{user_id}']
        del users[f'{user_id}']
        start(update, context)


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )

        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )

        updater = Updater(
            bot=bot,
            use_context=True,
        )
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, registerContact))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

        updater.start_polling()
        updater.idle()
