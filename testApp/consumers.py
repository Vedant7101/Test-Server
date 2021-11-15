import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class Users(WebsocketConsumer):

    def connect(self):

        self.name = self.scope['url_route']['kwargs']['name'].replace(' ', '_')

        self.room_name = 'users'
        self.room_group_name = 'user_group'

        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        async_to_sync(self.channel_layer.group_send)('user_group',
            {
                'type': 'channel_message',
                'message': self.name + ' joined the chat'
            }
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)('user_group',
            {
                'type': 'channel_message',
                'message': 'Message from ' + self.name + ' : ' + text_data
            }
        )

    def disconnect(self):
        pass

    def channel_message(self, event):
        message = event['message']

        self.send(message)