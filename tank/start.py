import json
from typing import Optional, Awaitable, Union

from tornado import websocket, web, ioloop
from tank.motor import MotorController


class Controller:

    motor = MotorController()

    class MoveHandler(websocket.WebSocketHandler):
        def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
            pass

        def __init__(self, controller):
            self.controller: Controller = controller
            super().__init__()

        def check_origin(self, origin):
            return True

        def open(self):
            print("Move WebSocket opened")
            #TODO send HIGH to STDBY GPIO

        def on_message(self, message):
            message_json = json.load(message)
            if message_json.command == "fwd":
                self.controller.motor.forward()
            elif message_json.command == "rev":
                self.controller.motor.reverse()
            elif message_json.command == "left":
                self.controller.motor.spin_left()
            elif message_json.command == "right":
                self.controller.motor.spin_left()
            elif message_json.command == "fwdleft":
                self.controller.motor.forward_left()
            elif message_json.command == "fwdright":
                self.controller.motor.forward_right()
            elif message_json.command == "revleft":
                self.controller.motor.reverse_left()
            elif message_json.command == "revright":
                self.controller.motor.reverse_right()
            elif message_json.command == "stop":
                self.controller.motor.all_stop()
            else:
                self.controller.motor.all_stop()

        def on_close(self):
            #TODO send LOW to STDBY GPIO
            self.controller.motor.all_stop()

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
        (r'/(.*)', Fallback)
    ])

    def start_server(self, port: int = 8082):
        self.app.listen(port)
        print("listening on " + str(port))
        ioloop.IOLoop.instance().start()
