import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.config import Config
WIDTH = 400
HEIGHT = 640
Config.set('graphics', 'width', WIDTH)
Config.set('graphics', 'height', HEIGHT)
Config.set('graphics', 'resizable', '0')  # 창 크기 변경 방지 (선택)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.graphics import Color, Ellipse

from kivy.core.window import Window

def hex_to_rgba(hex_code, alpha=1.0):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16) / 255.0
    g = int(hex_code[2:4], 16) / 255.0
    b = int(hex_code[4:6], 16) / 255.0
    return r, g, b, alpha
class FaceLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        eye_size = (WIDTH * 0.4, WIDTH * 0.4)
        pupil_size = (WIDTH * 0.3, WIDTH * 0.3)
        pupil_size2 = (WIDTH * 0.07, WIDTH * 0.07)

        # 왼쪽 눈 위치
        left_eye_x = Window.width * 0.2
        eye_y = Window.height * 0.5

        # 오른쪽 눈 위치
        right_eye_x = Window.width * 0.6

        # 안쪽 원은 바깥 원의 중앙에 배치
        def get_pupil_pos(eye_x, eye_y, eye_size, pupil_size):
            return (
                eye_x + (eye_size[0] - pupil_size[0]) / 2,
                eye_y + (eye_size[1] - pupil_size[1]) / 2
            )
        
        def get_pupil_pos2(eye_x, eye_y, eye_size, pupil_size):
            return (
                eye_x + (eye_size[0] - pupil_size[0]) - 5,
                eye_y + (eye_size[1] - pupil_size[1])
            )

        left_pupil_x, left_pupil_y = get_pupil_pos(left_eye_x, eye_y, eye_size, pupil_size)
        right_pupil_x, right_pupil_y = get_pupil_pos(right_eye_x, eye_y, eye_size, pupil_size)

        left_pupil_x2, left_pupil_y2 = get_pupil_pos2(left_pupil_x, eye_y, pupil_size, pupil_size2)
        right_pupil_x2, right_pupil_y2 = get_pupil_pos2(right_pupil_x, eye_y, pupil_size, pupil_size2)

        with self.canvas:
            # 눈 색상 (주황)
            rgba = hex_to_rgba('#FF7E1B')
            Color(*rgba)
            Ellipse(pos=(left_eye_x, eye_y), size=eye_size)
            Ellipse(pos=(right_eye_x, eye_y), size=eye_size)

            # 눈동자 (검정)
            Color(0, 0, 0, 1)
            Ellipse(pos=(left_pupil_x, left_pupil_y), size=pupil_size)
            Ellipse(pos=(right_pupil_x, right_pupil_y), size=pupil_size)

            # 눈동자 (하양)
            Color(1, 1, 1, 1)
            Ellipse(pos=(left_pupil_x2, left_pupil_y2), size=pupil_size2)
            Ellipse(pos=(right_pupil_x2, right_pupil_y2), size=pupil_size2)


class MyApp(App):
    def build(self):
        return FaceLayout()

if __name__ == '__main__':
    MyApp().run()

