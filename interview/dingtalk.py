#coding=utf-8
from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import json
from django.conf import settings

# def send(message, at_mobiles=[]):
#     # 引用 settings里面配置的钉钉群消息通知的WebHook地址:
#     webhook = settings.DINGTALK_WEB_HOOK
#
#     # 初始化机器人小丁, # 方式一：通常初始化方式
#     xiaoding = DingtalkChatbot(webhook)
#
#     # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
#     # xiaoding = DingtalkChatbot(webhook, secret=secret)
#
#     # Text消息@所有人
#     xiaoding.send_text(msg=('面试通知: %s' % message), at_mobiles = at_mobiles )

def send(msg):
    base_url = settings.DINGTALK_WEB_HOOK
    headers = {'Content-Type': 'application/json'}
    content = {
        "msgtype": "markdown",
        "markdown": {
            "title": "当前任务队列情况",
            "text": " ## push统计报告\n ### **进程心跳连接** \n>{} &emsp;&emsp;&emsp; result：{} \n>".format(msg, msg),
        },
        "at": {
             "atMobiles": [],# @人
            "isAtAll": False

        }
    }
    requests.post(url=base_url, headers=headers, proxies={}, data=json.dumps(content))

if __name__ == '__main__':
    send("ceshisdasdas")

