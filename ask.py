import os

import flask
import requests

app = flask.Flask(__name__)

SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL_WHITELIST = os.environ['CHANNEL_WHITELIST'].split()


@app.route('/ask', methods=['POST'])
def ask():
    if flask.request.form['token'] != SLACK_TOKEN:
        flask.abort(400)

    if flask.request.form['channel_name'] not in CHANNEL_WHITELIST:
        return flask.jsonify({
            'response_type': 'ephemeral',
            'text': 'Posting anonymously to %s is not allowed' % flask.request.form['channel_name']
        })

    r = requests.post(flask.request.form['response_url'], json={
        'response_type': 'in_channel',
        'text': 'Received anonymously:',
        'attachments': [
            {'text': flask.request.form['text']}
        ]
    })

    if r.status_code != 200:
        return flask.jsonify({
            'response_type': 'ephemeral',
            'text': 'Failed to post. Try again.'
        })

    return flask.jsonify({})


if __name__ == '__main__':
    app.run()