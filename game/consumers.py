import json
from channels.generic.websocket import AsyncWebsocketConsumer

class HostPanelConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "jeopardy_host"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "jeopardy_game_board", {"type": "game_update", "data": data}
        )

    async def game_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))


class GameBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "jeopardy_game_board"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def game_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
