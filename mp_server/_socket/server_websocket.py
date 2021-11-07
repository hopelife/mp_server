# -*- coding=utf-8 -*-
"""
주요 기능: 
    - 매매 신호 수신
    - 매매 결과 송신
    - 사용자 인증

사용례: 
    - 
"""

##@@@ 모듈 import
##============================================================

##@@ Built-In 모듈
##------------------------------------------------------------


##@@ Package 모듈
##------------------------------------------------------------


##@@ User 모듈
##------------------------------------------------------------


##@@@ 전역 상수/변수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 보조 함수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 실행 함수
##============================================================

##@@ Section
##------------------------------------------------------------

# https://stackoverflow.com/questions/42009202/how-to-call-a-async-function-contained-in-a-class

# import sys, json
# import asyncio
# from websockets import connect

# class EchoWebsocket:
#     async def __aenter__(self):
#         self._conn = connect('wss://ws.binaryws.com/websockets/v3')
#         self.websocket = await self._conn.__aenter__()        
#         return self

#     async def __aexit__(self, *args, **kwargs):
#         await self._conn.__aexit__(*args, **kwargs)

#     async def send(self, message):
#         await self.websocket.send(message)

#     async def receive(self):
#         return await self.websocket.recv()

# class mtest:
#     def __init__(self):
#         self.wws = EchoWebsocket()
#         self.loop = asyncio.get_event_loop()

#     def get_ticks(self):
#         return self.loop.run_until_complete(self.__async__get_ticks())

#     async def __async__get_ticks(self):
#         async with self.wws as echo:
#             await echo.send(json.dumps({'ticks_history': 'R_50', 'end': 'latest', 'count': 1}))
#             return await echo.receive()




# from testws import *

# a = mtest()

# foo = a.get_ticks()
# print (foo)

# print ("async works like a charm!")

# foo = a.get_ticks()
# print (foo)

# ## websocket_server1
# ##---------------------------------------------------------

# import asyncio 
# import websockets

# # call back for websockets.serve(accept,
# async def accept(websocket, path): 
#     while True:
#         data_rcv = await websocket.recv(); # receiving the data from client. 
#         print("received data = " + data_rcv); 
#         await websocket.send("websock_svr send data = " + data_rcv); # send received data

# # websocket server creation
# websoc_svr = websockets.serve(accept,"localhost", 7777)

# # waiting 
# asyncio.get_event_loop().run_until_complete(websoc_svr); 
# asyncio.get_event_loop().run_forever(); 


# ## websocket_server2
# ##---------------------------------------------------------

# import asyncio 
# import websockets

# CLIENTS = set()

# # async def broadcast():
# #     while True:
# #         for ws in CLIENTS:
# #             await ws.send("woof")
# #         await asyncio.sleep(2)

# # asyncio.create_task(broadcast())

# async def handler(websocket, path):
#     CLIENTS.add(websocket)
#     try:
#         # async for msg in websocket:
#         #     pass
#         while True:
#             for ws in CLIENTS:
#                 ## TODO: return message HERE
#                 await ws.send("woof")
#             await asyncio.sleep(2)
#     finally:
#         CLIENTS.remove(websocket)

# start_server = websockets.serve(handler,"localhost", 7777)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


# ## websocket_client1
# ##---------------------------------------------------------

# import asyncio 
# import websockets

# async def my_connect():
#     async with websockets.connect("ws://localhost:7777") as websocket:
#         for i in range(1,100,1):
#             await websocket.send("Hi server. I'm client" )
#             data_rcv = await websocket.recv(); 
#             print("data received from server : " + data_rcv); 

# # connect to server 
# asyncio.get_event_loop().run_until_complete(my_connect())


# ## websocket_client2
# ##---------------------------------------------------------

# import asyncio 
# import websockets

# async def my_connect():
#     async with websockets.connect("ws://localhost:7777") as websocket:
#         # for i in range(1,100,1):
#         #     await websocket.send("Hi server. I'm client" )
#         print("data from server : "); 
#         # while True:
#         for i in range(1,100,1):
#             data_rcv = await websocket.recv(); 
#             print("data from server : " + data_rcv)

# # connect to server 
# asyncio.get_event_loop().run_until_complete(my_connect())


if __name__ == "__main__":
    pass
