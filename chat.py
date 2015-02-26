from flask import Flask, flash, render_template, session, request, redirect, url_for, jsonify
from flask_sockets import Sockets
import time

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo')
def echo_socket(ws):

    while True:
        #message = ws.receive()
        comment_dict = {"author": "catmoon", 
                        "body": "test", 
                        "author_flair_css_class": "Heat1", 
                        "comment_id": "qwresdf", 
                        "score": "sdfsafd",
                        "created_utc": "123123123", 
                        "emitted": "true"}
        message = json.dumps({'message': comment_dict,'category':'comment', 'thread': 'asda'})
        ws.send(message)
        time.sleep(5)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/')
def hello():
    return \
'''
<html>

    <head>
        <title>Admin</title>

        <script type="text/javascript">
            var ws = new WebSocket("ws://" + location.host + "/echo");
            ws.onmessage = function(evt){ 
                    var received_msg = evt.data;
                    alert(received_msg);
            };

            ws.onopen = function(){
                ws.send("hello john");
            };
        </script>

    </head>

    <body>
        <p>hello world</p>
    </body>

</html>
'''

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
    app.run()