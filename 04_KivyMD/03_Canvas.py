from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Line


class canvas_Rectangle(Widget):
    pass

class canvas_CenterLine(Widget):
    pass

class canvas_Ellipse(Widget):
    pass


class canvas_Lines(Widget):
    pass

class Graph_Lines(Widget):
    pass

class New_Line(Widget):
    pass

class Touch(Widget):

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 0, 5, mode='rgba')
            self.rectangle = Rectangle(pos=(100, 0), size=(100, 100))
            Color(1, 0, 0, 1, mode='rgba')
            self.rectangle = Rectangle(pos=(200, 300), size=(100, 50))
            self.line = Line()

    def on_touch_up(self, touch):
        print('Touch_UP:', touch)

    def on_touch_down(self, touch):
        print('Touch_DOWN:', touch)
        self.rectangle.pos = touch.pos

    def on_touch_move(self, touch):
        print('Touch_MOVE', touch.pos)
        self.rectangle.pos=touch.pos
        # self.line.points=touch.pos


class canvasApp(App):
    def build(self):
        return canvas_CenterLine()


canvasApp().run()
