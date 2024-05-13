from processing_py import App
from math import cos, sin, radians

app = App(500, 500)
app.noStroke()
pcx=pcy=0

class Body:
    def __init__(self, cx, cy, sma, smi, speed):
        self.cx, self.cy, self.sma, self.smi, self.speed = cx, cy, sma, smi, speed * 20
        self.angle = 15

    def update(self):
        pcx=self.cx
        pcy=self.cy
        self.angle = (self.angle + self.speed) % 360
        return (self.cx + self.sma * cos(radians(self.angle)), self.cy + self.smi * sin(radians(self.angle)))

bodies = [Body(app.width / 2, app.height / 2, 50 + i * 25, 25 + i * 12.5, 0.1 - i * 0.015) for i in range(7)]

while True:

    app.background(0)
    for body in bodies:
        x, y = body.update()
        app.ellipse(x, y, 6, 6)
    app.ellipse(bodies[0].cx, bodies[0].cy, 10, 10)
    app.fill(255)
    app.redraw()