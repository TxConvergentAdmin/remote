from flask import Flask, request, jsonify
import pyautogui
import os


STATIC_PATH = os.path.join(os.path.dirname(__file__), '..', 'static')


app = Flask(__name__, static_url_path='', static_folder=STATIC_PATH)
config = {'master-code': 'convergent', 'temp-code': 'convergent'}


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/cmd", methods=['POST'])
def cmd():
    data = request.json
    code = data['code']
    type_ = data['type']
    value = data.get('value')
    name = data['name']
    assert code in [config['master-code'], config['temp-code']]
    if type_ == 'code':
        assert code == config['master-code']
        if name == 'temp':
            config['temp-code'] = value
        else:
            config['master-code'] = value
            config['temp-code'] = value
        return jsonify({'title': 'Success!', 'message': 'Code updated.'})
    elif type_ == 'control':
        if name == 'forward':
            pyautogui.press('right')
        elif name == 'back':
            pyautogui.press('left')
    return jsonify({})


@app.errorhandler(AssertionError)
def handle_assert(err):
    return jsonify({'title': 'Access Denied', 'message': 'Your code is invalid.'}), 200