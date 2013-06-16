from arduino import Arduino
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

arduino = Arduino("COM6", 9600)


class SimpleEcho(WebSocket):

    def handleMessage(self):
        if self.data is None:
            self.data = ''

        # echo message back to client
        self.sendMessage(str(self.data))

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()
