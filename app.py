from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('c5d4HO2JNGbKKQSSGnu7QiOCf0/+/ROYQUS3taDxc/xSEn68ZN+EiFEgQdtDn4429MrvhKyE1sJ6u8Feu6dG3bOWZfpse/mvsuzGk08Mqtrek0iF+7TUQEMRn5cwbsAHUASgtWu2zdrR9lhgcFas5gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2b1ddbe9c87280e1ac453de1cf0c5ac3')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說什麼'
    
    if msg == 'hi':
        r = 'hello,你好！'
    elif msg == '你吃飯了嗎？'：
        r = 'not yet'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()