import json
import ssl
from typing import Optional, Awaitable, Union

from tornado import websocket, web, ioloop, httpserver
from tank.motor import MotorController

motor = MotorController()
ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain("/etc/ssl/certs/cert.pem", "/etc/ssl/certs/key.pem")


class Controller:

    class MoveHandler(websocket.WebSocketHandler):
        def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
            pass

        def check_origin(self, origin):
            return True

        def open(self):
            #TODO implement logging
            print("Move WebSocket opened")
            motor.board_init()

        def on_message(self, message):
            #TODO implement logging
            message_json = json.loads(message)
            if message_json["command"] == "fwd":
                motor.forward(message_json["speed"])
            elif message_json["command"] == "rev":
                motor.reverse(message_json["speed"])
            elif message_json["command"] == "spinleft":
                motor.spin_left(message_json["speed"])
            elif message_json["command"] == "spinright":
                motor.spin_right(message_json["speed"])
            elif message_json["command"] == "fwdleft":
                motor.forward_left(message_json["speed"])
            elif message_json["command"] == "fwdright":
                motor.forward_right(message_json["speed"])
            elif message_json["command"] == "revleft":
                motor.reverse_left(message_json["speed"])
            elif message_json["command"] == "revright":
                motor.reverse_right(message_json["speed"])
            elif message_json["command"] == "stop":
                motor.all_stop()
            else:
                motor.all_stop()

        def on_close(self):
            #TODO implement logging
            motor.all_stop()
            motor.board_shutdown()

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

    server = httpserver.HTTPServer(app, ssl_options=ssl_ctx)

    def start_server(self, port: int = 8082):
        self.server.listen(port)
        print("listening on " + str(port))
        ioloop.IOLoop.instance().start()
