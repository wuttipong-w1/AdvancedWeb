from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "wuttipong happy 2021"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)