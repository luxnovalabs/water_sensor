from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):
	print 'something echoed'
	while not ws.closed:
		message = ws.receive()
		ws.send(message)

@app.route('/')
def hello():
	print 'something helloed'
	return 'Hello World!'


if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()