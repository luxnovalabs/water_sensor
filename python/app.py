from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

import json as JSON

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

######################################################
#################### EXAMPLES ########################
######################################################
# #from flask quickstart http://flask.pocoo.org/docs/0.10/quickstart/
# @app.route('/')
# def hello_world():
# 		return 'Hello World!'

# #just showing how to load a template
# @app.route('/test_template')
# @app.route('/test_template/<name>')
# def test_template(name=None):
# 	return render_template('hello.html', name=name)


#from flask-scoketio getting started : https://flask-socketio.readthedocs.org/en/latest/

# #they arent very clear, but you generally first serve a webpage that ha some javascript in it that triggers the socket stuff form the client side
# @app.route('/hello_sockets')
# def hello_sockets():
# 		return render_template('hello_sockets.html')

# # this will come from client
# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))

######################################################
#################### OUR APP #########################
######################################################

#hacking together a barebones angular example from this : https://realpython.com/blog/python/flask-by-example-integrating-flask-and-angularjs/
@app.route('/')
def index():
	return render_template('angular_with_sockets.html')

@socketio.on('connect')
def connect():
	print 'someone has joined the server'
	emit('get_moisture_value', 'please') 

# this will come from client
@socketio.on('ping_server')
def ping_server(json):
	print('client says: ' + str(json))

# this will come from client
@socketio.on('receiving_sensor_update')
def receiving_sensor_update(json):
	print('sensor says: ' + str(json))



if __name__ == '__main__':
	socketio.debug = False
	socketio.run(app, host='0.0.0.0')









