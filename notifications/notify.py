# -*- coding: utf8 -*-
from django.conf import settings
from food.models import FoodUser
from parse_rest import connection

from .tasks import async_push

# TODO: move to app config
connection.register(settings.PARSE_APPLICATION_ID, settings.PARSE_REST_API_KEY)


class Event:
    FOOD_AVAILABLE = 'FoodAvailable'


def data_dict(alert, event, sound=None, badge=None):
    ret = {
        'alert': alert,
        'pierogi_event': event,
    }

    if sound:
        ret['sound'] = sound

    if badge:
        ret['badge'] = badge

    return ret


def push_notification(alert, event, users, sound=None, badge=None):
    for user in users:
        data = data_dict(alert, event, sound=sound, badge=badge)
        data['pierogi_event']['to'] = user.email

        # Send to the user's most recently used device
        device = user.devices.order_by('-last_login_at').first()
        # User logged in using a real device
        if device and device.is_active:
            async_push.delay(data, {'deviceToken': device.device_token})


def make_food_event(food, event_type, **kwargs):
    event = {
        'type': event_type,
        'food_name': food.name
    }

    event.update(kwargs)

    return event


def food_available(food):
    """
    Notify Scout that they have been added to a campaign.
    """
    users = FoodUser.objects.filter(company=food.giver.company, should_be_notified=True)
    event = make_food_event(food, Event.FOOD_AVAILABLE)
    message = 'Food ({}) is available for the taking in the {}'.format(food.name, food.place.name)

    push_notification(message, event, users)

