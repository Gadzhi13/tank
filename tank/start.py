import json
from typing import Optional, Awaitable, Union

from tornado import websocket, web, ioloop
from tank.motor import MotorController

motor = MotorController()


class Controller:

    class MoveHandler(websocket.WebSocketHandler):
        def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
            pass

        def check_origin(self, origin):
            return True

        def open(self):
            print("Move WebSocket opened")
            #TODO send HIGH to STDBY GPIO

        def on_message(self, message):
            message_json = json.loads(message)
            if message_json["command"] == "fwd":
                motor.forward()
            elif message_json["command"] == "rev":
                motor.reverse()
            elif message_json["command"] == "left":
                motor.spin_left()
            elif message_json["command"] == "right":
                motor.spin_left()
            elif message_json["command"] == "fwdleft":
                motor.forward_left()
            elif message_json["command"] == "fwdright":
                motor.forward_right()
            elif message_json["command"] == "revleft":
                motor.reverse_left()
            elif message_json["command"] == "revright":
                motor.reverse_right()
            elif message_json["command"] == "stop":
                motor.all_stop()
            else:
                motor.all_stop()

        def on_close(self):
            #TODO send LOW to STDBY GPIO
            motor.all_stop()

    class EchoWebSocket(websocket.WebSocketHandler):
        def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
            pass

        def check_origin(self, origin):
            return True

        def open(self):
            print("Echo WebSocket opened")

        def on_message(self, message):
            self.write_message(u"You said: " + message)

        def on_close(self):
            print("Echo WebSocket closed")

    class Fallback(websocket.WebSocketHandler):
        def on_message(self, message: Union[str, bytes]) -> Optional[Awaitable[None]]:
            pass

        def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
            pass

        def check_origin(self, origin):
            return True

        def open(self):
            print("Error initialising handler")
            self.close(1011, "Error initialising handler")

    app = web.Application([
        (r'/move', MoveHandler),
        (r'/echo', EchoWebSocket),
        (r'/.*', Fallback)
    ])

    def start_server(self, port: int = 8082):
        self.app.listen(port)
        print("listening on " + str(port))
        ioloop.IOLoop.instance().start()
