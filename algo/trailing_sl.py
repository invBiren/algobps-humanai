class TrailingSL:
    def __init__(self, trail_points):
        self.trail = trail_points
        self.high = None
        self.sl = None

    def update(self, price):
        if self.high is None or price > self.high:
            self.high = price
            self.sl = price - self.trail

        return self.sl
