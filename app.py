from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
URL = f'https://api.telegram.org/bot{TOKEN}/'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data['message']['chat']['id']
        if "text" in data['message']:
            text = data['message']['text']
            if text == "/start":
                send_message(chat_id, "Hello! Click the button below to visit our website.")
                send_button(chat_id)
    return '', 200

def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(URL + 'sendMessage', json=payload)

def send_button(chat_id):
    button = {
        'inline_keyboard': [
            [{'text': 'Visit Website', 'url': 'https://your-wordpress-site.com'}]
        ]
    }
    payload = {
        'chat_id': chat_id,
        'text': 'Click the button below:',
        'reply_markup': button
    }
    requests.post(URL + 'sendMessage', json=payload)

if __name__ == '__main__':
    app.run(debug=True)
