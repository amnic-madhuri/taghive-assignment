from flask import Flask, request
import requests
application = Flask(__name__)


@application.route('/hello')
def hello():
    return 'Hello there'


@application.route('/jobs', methods=['POST'])
def jobs():
    token = request.headers['Authorization']
    data = {"token": token}
    output = requests.post('http://192.168.59.100:30002/auth', data=data).content
    result = output.decode()
    if result == "density":
        return 'Jobs:\nTitle: Devops\nDescription: Awesome\n'
    else:
        return 'fail'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
