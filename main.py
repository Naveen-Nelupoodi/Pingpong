from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint



class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball, paddle):
        if self.collide_widget(ball):
            ball.velocity_y *= -1
            ball.velocity_y += 0.2
            ball.velocity_x += 0.2
            paddle.score += 1


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    paddle = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(0, 10).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        if self.ball.y < 0:
            self.ball.velocity_y *= -1
            self.paddle.score -= 1
        if self.ball.y > self.height - 150:
            self.ball.velocity_y *= -1
        if (self.ball.x < 10) or (self.ball.x > self.width - 60):
            self.ball.velocity_x *= -1
        self.paddle.bounce_ball(self.ball, self.paddle)
       
    def on_touch_move(self, touch):
        self.paddle.center_x = touch.x



class PingApp(App):
    def build(self):
        

        #Game
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)

        return game


if __name__ == '__main__':
    PingApp().run()
