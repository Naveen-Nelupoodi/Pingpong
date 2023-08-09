from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
#Video
#import cv2
#from kivy.uix.image import Image
#from kivy.graphics.texture import Texture


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
        #global loc
        #self.paddle.center_x = int((self.width / 520) *(520- loc))

    def on_touch_move(self, touch):
        self.paddle.center_x = touch.x



class PingApp(App):
    def build(self):
        # Video
        #global loc
        #loc =0
        #self.image = Image()
        #self.face_facade = cv2.CascadeClassifier("haarcascade_frontal_face.xml")
        #self.capture = cv2.VideoCapture(0)
        #Clock.schedule_interval(self.load_video, 1.0 / 30.0)

        #Game
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)

        return game

    #def load_video(self, *args):
        #ret, frame = self.capture.read()
        #frame initialize
        #self.image_frame = frame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #object = self.face_facade.detectMultiScale(gray, 1.3, 4)
        #for (x, y, w, h) in object:
            #global loc
            #loc = x
            #cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 5)
            #print(x,y)
        #buffer = cv2.flip(gray, -1).tobytes()
        #texture = Texture.create(size=(gray.shape[1], gray.shape[0]), colorfmt = 'luminance')
        #texture.blit_buffer(buffer, colorfmt='luminance', bufferfmt='ubyte')
        #self.root.ids.vid.texture = texture

if __name__ == '__main__':
    PingApp().run()