# appname/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PredictTextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_predicted_text(self, text):
        await self.send(text)

    @staticmethod
    async def broadcast(text):
        # Broadcast the predicted text to all connected WebSocket clients
        await PredictTextConsumer().channel_layer.group_add("predict_text_group", PredictTextConsumer().channel_name)
        await PredictTextConsumer().channel_layer.group_send(
            "predict_text_group",
            {"type": "send.predicted_text", "text": text},
        )

    async def send_predicted_text(self, text):
        await self.send(text)

    async def send_predicted_text(self, event):
        text = event["text"]
        await self.send(text)
