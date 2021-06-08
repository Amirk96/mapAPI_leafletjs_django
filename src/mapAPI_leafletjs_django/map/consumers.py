''' from channels.consumer import SyncConsumer

class EchoConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
    
    def websocket_disconnect(self, event):
        print('Disconnected', event)
 '''

from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, async_to_sync

class EchoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name='group_data'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        print('Disconnected', close_code)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self,text_data):

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'randomFunction',
                'value':text_data,
            }
        )

    async def randomFunction(self,event):
        print (event['value'])
        await self.send(event['value'])
