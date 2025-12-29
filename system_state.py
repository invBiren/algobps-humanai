class SystemState:
    def __init__(self):
        # Core
        self.health = "ok"          # ok | degraded | halted
        self.mode = "paper"         # paper | live
        self.live_enabled = False

        # Messaging
        self.last_change_reason = "System started in safe mode"
        self.alerts = []

    # ----- Mode Control -----
    def request_live(self):
        return {
            "allowed": False,
            "reason": "Live trading requires explicit approval"
        }

    def approve_live(self):
        self.mode = "live"
        self.live_enabled = True
        self.last_change_reason = "User approved live trading"

    def set_paper(self):
        self.mode = "paper"
        self.live_enabled = False
        self.last_change_reason = "Switched back to paper mode"

    # ----- Alerts -----
    def add_alert(self, level, message, fix=None):
        self.alerts.append({
            "level": level,
            "message": message,
            "fix": fix
        })

    def clear_alerts(self):
        self.alerts = []


SYSTEM_STATE = SystemState()
