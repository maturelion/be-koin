from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import AnonymousUser
import json

from wallets.models import Wallet

class BalanceConsumer(WebsocketConsumer):
    def connect(self):
        # Check if user is authenticated
        if self.scope['user'] == AnonymousUser():
            self.close()
        else:
            user = self.scope['user']
            print(user)
        self.accept()
        

        # Fetch the balance from the database or any other source
        wallet = Wallet.objects.get(user=user.id)

        # Send the balance to the frontend
        self.send(json.dumps({'balance': wallet.balance}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
