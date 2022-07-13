"""
WebSocket manager handling connection/disconnection
"""

from fastapi.concurrency import run_until_first_complete
from fastapi import WebSocket
from broadcaster import Broadcast
from ..utils.utils import setting


class GameManager(object):

    def __int__(self):
        self.broadcast = Broadcast(
            url="postgres://{}:{}@{}/{}".format(setting.database_username, setting.database_password,
                                                setting.database_hostname + ":" + setting.database_port,
                                                setting.database_name)
        )

    async def connectService(self):
        await self.broadcast.connect()

    async def disconnectService(self):
        await self.broadcast.disconnect()

    async def gameRoomWebSocket(self, websocket: WebSocket, gameid: str):
        await websocket.accept()
        await run_until_first_complete(
            (self.gameRoomReceiver, {"websocket": websocket, "gameid": gameid}),
            (self.gameRoomSender, {"websocket": websocket, "gameid": gameid})
        )

    async def gameRoomReceiver(self, websocket: WebSocket, gameid: str):
        async for message in websocket.iter_text():
            await self.broadcast.publish(channel=str(gameid), message=message)

    async def gameRoomSender(self, websocket: WebSocket, gameid: str):
        async with self.broadcast.subscribe(channel=str(gameid)) as gameSubscriber:
            async for event in gameSubscriber:
                await websocket.send_text(event.message)
