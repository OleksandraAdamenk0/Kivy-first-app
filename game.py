from random import randint

from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from pong_ball import PongBall
from player import PongPlayer


class PongGame(Widget):
    ball = ObjectProperty(None)
    player_1 = ObjectProperty(None)
    player_2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        Window.bind(on_resize=self.on_resize)

    def on_resize(self, wd, w, h):
        self.serve_ball()

    def serve_ball(self, dt=None):
        self.ball.center = self.center
        self.ball.velocity = Vector(self.width / 100, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        self.check_collisions()

        self.player_1.bounce_ball(self.ball)
        self.player_2.bounce_ball(self.ball)

        self.check_bounds()

    def check_bounds(self):
        if self.ball.x < self.x:
            self.player_2.score += 1
            self.serve_ball()
        if self.ball.right > self.width:
            self.player_1.score += 1
            self.serve_ball()

    def check_collisions(self):
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player_1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player_2.center_y = touch.y
