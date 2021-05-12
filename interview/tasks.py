from __future__ import absolute_import, unicode_literals
"""
消息同志celery 异步推送
"""
from celery import shared_task 
# from .dingtalk import send
from interview.dingtalk import send

@shared_task
def send_dingtalk_message(message):
    send(message)

if __name__ == '__main__':
    send_dingtalk_message('dasda')