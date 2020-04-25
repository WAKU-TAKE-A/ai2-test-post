#-*-coding:utf-8;-*-

import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/post',methods=["POST"])
def test_post():
    print(request.headers)
    str_enc = request.json['image']
    bin_dec = base64.urlsafe_b64decode(
        str_enc + '=' * (-len(str_enc) % 4))
    fnm = 'C:/tmp/flsk-test-post/tmp000.jpg'
    with open(fnm, "wb") as f:
        f.write(bin_dec)
    return '{"json":{"image":"' + str_enc + '"}}'
