from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'daniel/gremio' 

socketio = SocketIO(app) 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    print(f"Alguém enviou: {msg}") 
    
    send(msg, broadcast=True) 

if __name__ == '__main__':
    # O host='0.0.0.0' avisa o servidor para aceitar conexões de qualquer aparelho na rede
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 