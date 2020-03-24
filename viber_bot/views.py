from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

from viberbot.api.messages import TextMessage, KeyboardMessage, PictureMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberSubscribedRequest, ViberMessageRequest

from .models import ViberUser

bot_configuration = BotConfiguration(
    name='доктор Киреева',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4b2fa578ca67d1cb-3c3f935ff2cc70ff-2d6ae53161c7920f')

viber = Api(bot_configuration)


@csrf_exempt
def set_webhook(request):
    event_types = ["failed",
                   "subscribed",
                   "unsubscribed",
                   "conversation_started"]
    url = f'https://{settings.ALLOWED_HOSTS[0]}/viber/callback/'
    viber.set_webhook(url=url, webhook_events=event_types)
    return HttpResponse('Ok')


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)

        if isinstance(viber_request, ViberConversationStartedRequest):
            viber.send_messages(viber_request.user.id, [
                TextMessage(text='Вас приветствует ассистет, что бы начать разговор напишите мне')
            ])

        elif isinstance(viber_request, ViberSubscribedRequest):
            pass

        elif isinstance(viber_request, ViberMessageRequest):
            ViberUser.objects.update_or_create(viber_id=viber_request.sender.id,
                                               defaults={
                                                   'is_active': True,
                                                   'name': viber_request.sender.name,
                                                   'language': viber_request.sender.language,
                                                   'country': viber_request.sender.country,
                                                   'api_version': viber_request.sender.api_version,

                                               }
                                               )

            if isinstance(viber_request.message, TextMessage):
                font_color = '#5080ab'
                text_size = 'large'
                text_color = '\"#F0FFFF\"'

                keyboard_home = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 3,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Консультация</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "reply",
                        "ActionBody": "консультация"
                    },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Услуги</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "услуги"
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Запись на прием</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "open-url",
                            "ActionBody": "tel:0989619257",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Местонахождение</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Местонахождение",

                        }
                    ]
                }
                keyboard_location = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Записаться на прием</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "open-url",
                        "ActionBody": "tel:0989619257",
                    },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Проложить маршрут</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "open-url",
                            "ActionBody": "https://goo.gl/maps/zyCpd4FJ2o5U4GKL7",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Главное меню</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Главное меню",
                        },
                    ]
                }
                keyboard_service = {
                    "Type": "keyboard",
                    "Buttons": [
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Блокада</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Блокада",
                        },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Плазмотерапия</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Плазмотерапия",
                        },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Метод RANC</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Метод RANC",
                        },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Капилляромезотерапия позвоночника</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Капилляромезотерапия позвоночника",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Главное меню</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Главное меню",
                        },
                    ]
                }
                keyboard_service_2 = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 3,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Паравертебральная</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "reply",
                        "ActionBody": "Паравертебральная",
                    },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Корешковая</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Корешковая",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Внутрисуставная</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Внутрисуставная",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Вернуться</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Вернуться",
                        },
                    ]
                }
                keyboard_service_3 = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 3,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Шейно-воротниковая зона</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "reply",
                        "ActionBody": "Шейно-воротниковая зона",
                    },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Волосистая часть головы</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Волосистая часть головы",
                        },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Суставов</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Суставов",
                        },
                        {
                            "Columns": 3,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Позвоночника</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Позвоночника",
                        },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Вернуться</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Вернуться",
                        },
                    ]
                }
                keyboard_exit = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Записаться на прием</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "open-url",
                        "ActionBody": "tel:0989619257",
                    },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Главное меню</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Главное меню",
                        }
                    ]
                }
                keyboard_exit_service = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Записаться на прием</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "open-url",
                        "ActionBody": "tel:0989619257",
                    },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Вернуться</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Вернуться",
                        },
                    ]
                }
                keyboard_exit_service_list = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Записаться на прием</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "open-url",
                        "ActionBody": "tel:0989619257",
                    },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Вернуться</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Блокады",
                        },
                    ]
                }
                keyboard_exit_service_list_2 = {
                    "Type": "keyboard",
                    "Buttons": [{
                        "Columns": 6,
                        "Rows": 1,
                        "Text": "<font color=" + text_color + "><b>Записаться на прием</b></font>",
                        "TextSize": text_size,
                        "BgColor": font_color,
                        "ActionType": "open-url",
                        "ActionBody": "tel:0989619257",
                    },
                        {
                            "Columns": 6,
                            "Rows": 1,
                            "Text": "<font color=" + text_color + "><b>Вернуться</b></font>",
                            "TextSize": text_size,
                            "BgColor": font_color,
                            "ActionType": "reply",
                            "ActionBody": "Плазмотерапия",
                        },
                    ]
                }

            text = viber_request.message.text
            # tracking_data = viber_request.message.tracking_data
            # message_user = ''
            if text == 'услуги':
                viber.send_messages(viber_request.sender.id, [TextMessage(text='это раздел услуги'),
                                                              KeyboardMessage(keyboard=keyboard_service)])
            elif text == 'консультация':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/blokadi.jpg')

                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Консультация невролога 250 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit)])
            elif text == 'Местонахождение':
                viber.send_messages(viber_request.sender.id,
                                    [TextMessage(text='г. Запорожье\nул. Троицкая, 27\nПн-Сб с 8.20 до 18.00'),
                                     KeyboardMessage(keyboard=keyboard_location)])
            elif text == 'Блокада' or text == 'Блокады':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/blokada.jpg')
                viber.send_messages(viber_request.sender.id,
                                    [message,
                                     TextMessage(text='Препараты для блокады от 200 грн. (подбираются индивидуально'),
                                     KeyboardMessage(keyboard=keyboard_service_2)])
            elif text == 'Плазмотерапия':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/plazmo.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Плазмотерапия'),
                                                              KeyboardMessage(keyboard=keyboard_service_3)])
            elif text == 'Метод RANC':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/metod_ranc.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Метод RANC 600 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service)])
            elif text == 'Капилляромезотерапия позвоночника':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/kapilaromezoter.jpg')
                viber.send_messages(viber_request.sender.id,
                                    [message,
                                     TextMessage(text='Капилляромезотерапия позвоночника 800 грн.'),
                                     KeyboardMessage(keyboard=keyboard_exit_service)])
            elif text == 'Главное меню':
                viber.send_messages(viber_request.sender.id, [TextMessage(text='Пожалуйста сделайте свой выбор'),
                                                              KeyboardMessage(keyboard=keyboard_home)])
            elif text == 'Вернуться':
                viber.send_messages(viber_request.sender.id, [TextMessage(text='это раздел усуги'),
                                                              KeyboardMessage(keyboard=keyboard_service)])
            elif text == 'Паравертебральная':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/paraverterbalnaj.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Блокада паравертербальная 400 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service_list)])
            elif text == 'Корешковая':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/paraverterbalnaj_1.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Блокада корешковая 500 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service_list)])
            elif text == 'Внутрисуставная':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/sustav.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Блокада внутрисуставная 600 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service_list)])
            elif text == 'Шейно-воротниковая зона':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/sheaj.jpg')
                viber.send_messages(viber_request.sender.id,
                                    [message,
                                     TextMessage(text='Плазмотерапия шейно-воротниковой зоны 800 грн.'),
                                     KeyboardMessage(keyboard=keyboard_exit_service_list_2)])
            elif text == 'Волосистая часть головы':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/volos.jpg')
                viber.send_messages(viber_request.sender.id,
                                    [message,
                                     TextMessage(text='Плазмотерапия волосистой части головы 1100 грн.'),
                                     KeyboardMessage(keyboard=keyboard_exit_service_list_2)])
            elif text == 'Суставов':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/plazmo_sustav.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Плазмотерапия суставов от 600 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service_list_2)])
            elif text == 'Позвоночника':
                message = PictureMessage(
                    media=f'https://{settings.ALLOWED_HOSTS[0]}/media/paraverterbalnaj.jpg')
                viber.send_messages(viber_request.sender.id, [message,
                                                              TextMessage(text='Плазмотерапия одного отдела 800 грн.'),
                                                              KeyboardMessage(keyboard=keyboard_exit_service_list_2)])
            else:
                keyboard_message = KeyboardMessage(keyboard=keyboard_home)
                viber.send_messages(viber_request.sender.id, [keyboard_message])

    return HttpResponse(status=200)


class ViberUserView(View):
    def get(self, request):
        return HttpResponse('Hi')
