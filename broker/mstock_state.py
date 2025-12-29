class MStockState:
    def __init__(self):
        self.connected = False
        self.client_code = None
        self.last_message = "Not connected"

    def set_connected(self, client_code):
        self.connected = True
        self.client_code = client_code
        self.last_message = "Authenticated successfully"

    def set_disconnected(self, msg):
        self.connected = False
        self.client_code = None
        self.last_message = msg


MSTOCK_STATE = MStockState()
