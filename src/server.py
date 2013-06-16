import json
import time

from twisted.internet import reactor
from autobahn.websocket import (
    WebSocketServerFactory,
    WebSocketServerProtocol,
    listenWS,
)

from arduino import Arduino

arduino = Arduino("COM6", 19200)


class EchoServerProtocol(WebSocketServerProtocol):

    def onMessage(self, msg, binary):
        msg = json.loads(msg)
        x = msg.get("x", 0)
        y = msg.get("y", 0)
        r = msg.get("r", 0)
        g = msg.get("g", 0)
        b = msg.get("b", 0)
        arduino.change_color(x, y, r, g, b)
        time.sleep(.02)

if __name__ == '__main__':
    factory = WebSocketServerFactory("ws://localhost:9000")
    factory.protocol = EchoServerProtocol
    listenWS(factory)
    reactor.run()
