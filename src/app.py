from flask import Flask, jsonify, render_template, request
import socket

app = Flask(__name__)

def getDetails():
    ip = jsonify('ip', request.remote_addr)
    hostname = ('hostname', socket.gethostname())
    return ip, hostname
@app.route("/")
def list_endpoints():
    return "try using one of my many exciting endspoints, /hello, /health, /test"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
        return jsonify(
            status="UP"
        )


@app.route("/test")
def test():
    ip, hostname = getDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)