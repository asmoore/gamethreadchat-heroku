import sys
from chat import ChatBackend, app

def publish_message(user, message):
        chat = ChatBackend()
        message = "{'handle': user, 'text': message}"
        chat.publish(message)

        
if __name__ == '__main__': 
    if '-publish_message' in sys.argv: 
        publish_message('test user', 'test message') 
