# -*- coding: utf8 -*-
from celery import shared_task
from celery.utils.log import get_task_logger
from parse_rest import installation
from parse_rest.core import ParseError


logger = get_task_logger(__name__)

@shared_task(default_retry_delay=10)
def async_push(data, where):
    try:
        ev = data['pierogi_event']
        logger.info('Pushing "%s" to user %s (token=%s)',
            data['alert'], ev['to'], where.get('deviceToken'))
        installation.Push.alert(data, where)
    except ParseError:
        async_push.retry()
