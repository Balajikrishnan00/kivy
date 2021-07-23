from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics.vertex_instructions import Line
from kivy.metrics import dp


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

class canvas_Example3(Widget):
    pass

class Canvas_Example4(Widget):
    def __init__(self,**kwargs):
        super(Canvas_Example4, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(0,0,100,100),width=2)
            Color(0,1,0)
            Line(points=(200,200,300,300),width=2)
            Line(circle=(200,300,100))
            Line(points=(0,0,200,300))
            Line(circle=(200,200,100,))
            Line(rectangle=(300,300,400,200))
            Line(ellipse=(500,200,100,80))
            self.rec=Rectangle(pos=(300,200),size=(200,100))
    def on_Button_Click(self):

        print('Foo')
        x,y=self.rec.pos
        x+=dp(10)
        y+=dp(10)
        w,h=self.rec.size
        self.rec.pos=(x,y)
        print(x,y)
        print(w,h)








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
        return Canvas_Example4()


canvasApp().run()
