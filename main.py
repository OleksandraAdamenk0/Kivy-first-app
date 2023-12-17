# This is a sample kivy game.
import kivy
from kivy.app import App
from kivy.clock import Clock

from game import PongGame


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_once(game.serve_ball, 0)
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
