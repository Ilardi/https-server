from flask import Flask
import ssl

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, HTTPS!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
