import os

import flask
import requests

app = flask.Flask(__name__)

SLACK_TOKEN = os.environ['SLACK_TOKEN']
WEBHOOK_URL = os.environ['WEBHOOK_URL']


@app.route('/', methods=['POST'])
def anonymize():
    if flask.request.form['token'] != SLACK_TOKEN:
        flask.abort(400)

    text = flask.request.form['text'].strip()

    if not text:
        return flask.jsonify({
            'response_type': 'ephemeral',
            'text': "Can't send empty text!"
        })

    r = requests.post(WEBHOOK_URL, json={
        'text': 'Received anonymously:',
        'attachments': [{'text': text}]
    })

    if r.status_code != 200:
        return flask.jsonify({
            'response_type': 'ephemeral',
            'text': 'Failed to post. Try again: ' + r.text
        })

    requests.post(flask.request.form['response_url'], json={
        'response_type': 'ephemeral',
        'text': 'Anonymous comment submitted!',
        'attachments': [
            {'text': text}
        ]

    })

    return ('', 200)


if __name__ == '__main__':
    app.run()
