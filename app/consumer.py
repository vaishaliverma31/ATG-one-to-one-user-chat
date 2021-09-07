from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from asgiref.sync import async_to_sync
import json
from django.core.validators import ValidationError
from .models import User
from django.contrib.auth.models import Group
from .models import  User,  chatroom,get_or_create_personal_thread
from channels.auth import login
from channels.auth import login



class ChatConsumer(WebsocketConsumer,AsyncConsumer):
    def connect(self):
            other_username=self.scope['url_route']['kwargs']['username']
            sd = self.scope['user']
            senduser=User.objects.get(is_superuser=True)
            receiveruser=User.objects.get(username=other_username)
            thread_obj=get_or_create_personal_thread(senduser, receiveruser)
            print(thread_obj)
            self.room_name=f'personal_thread_{thread_obj}'
            self.update_user_status(senduser, 'online')
            async_to_sync(self.channel_layer.group_add)(
                self.room_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        user = self.scope['user']
        self.update_user_status(user, 'offline')

        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def receive(self, text_data):
        print(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_name, {
                'type':'chat_message',
                'message': text_data,
            }
        )

    def chat_message(self, event):
        message = event['message']
        data = json.loads(message)
        user=self.scope['user']
        id=User.objects.get(username=user)
        id1=id.id
        self.send(text_data=json.dumps({
            'message': data['message'],
            'image':data['image'],
            'id':id1,
            'recerid': data['id']

        }))
    def update_user_status(self, user, status):
        return User.objects.filter(pk=user.pk).update(status=status)



