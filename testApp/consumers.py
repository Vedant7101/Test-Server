import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class Users(WebsocketConsumer):

    def connect(self):

        room_name = self.scope['url_route']['kwargs']['name'].replace(' ', '_')

        self.room_name = room_name
        self.room_group_name = room_name + '_group'

        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,
            {
                'type': 'channel_message',
                'message': text_data
            }
        )

    def disconnect(self):
        pass

    def channel_message(self, event):
        message = event['message']

        self.send(message)