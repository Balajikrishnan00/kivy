from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics.vertex_instructions import Line, Ellipse
from kivy.metrics import dp
from kivy.properties import BooleanProperty,StringProperty
from kivy.properties import Clock


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

    is_enable=BooleanProperty(False)
    tongle_text=StringProperty('OFF')
    def __init__(self,**kwargs):
        super(Canvas_Example4, self).__init__(**kwargs)

        with self.canvas:
            #Line(points=(0,0,100,100),width=2)
            #Color(0,1,0)
            #Line(points=(200,200,300,300),width=2)
            #Line(circle=(200,300,100))
            #Line(points=(0,0,200,300))
            #Line(circle=(200,200,100,))
            #Line(rectangle=(300,300,400,200))
            #Line(ellipse=(500,200,100,80))
            self.rec=Rectangle(pos=(200,100),size=(50,50))
    def on_Button_Right(self):
        print('Foo')
        x,y=self.rec.pos
        w,h=self.rec.size
        inc=dp(10)
        diff=self.width-(x+w)
        print(self.width,x,w)
        print(diff<inc)
        if diff<inc:
            inc=diff
        x+=inc
        self.rec.pos=(x,y)
    def on_Button_Up(self):
        x, y = self.rec.pos
        w, h = self.rec.size
        inc=dp(10)
        diff = self.height -(y+h)
        if diff<inc:
            inc=diff
        y+=inc
        self.rec.pos=(x,y)

    def on_Button_Left(self):
        x,y=self.rec.pos
        w,h=self.rec.size
        inc=dp(10)
        print(x,y,w,h,inc)
        if x==0:
            inc=x
        else:
            x-=10
        self.rec.pos=(x,y)
    def on_Button_Down(self):
        x,y=self.rec.pos
        w,h=self.rec.size
        inc=dp(10)
        if y==0:
            inc=y
        else:
            y-=10
        self.rec.pos=(x,y)
    def tongle_Enable(self,widget):
        #print(widget.state)
        if widget.state=='normal':
            self.is_enable=False
            print(self.is_enable)
            self.tongle_text='OFF'
        else:
            #print(self.is_enable)
            self.is_enable=True
            print(self.is_enable)
            self.tongle_text='ON'

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

class ball_Amination(Widget):
    def __init__(self,**kwargs):
        super(ball_Amination, self).__init__(**kwargs)
        with self.canvas:
            self.ball=Ellipse(pos=(self.center),size=(50,50))

class canvas_Example6(Widget):
    def __init__(self,**kwargs):
        super(canvas_Example6, self).__init__(**kwargs)
        with self.canvas:
            self.rectangle=Rectangle(pos=(100,100),size=(100,100))

    def moveR(self):
        x,y=self.rectangle.pos
        w,h=self.rectangle.size
        x1=self.width-w
        m=10
        if x==x1:
            print(x,x1)
        else:
            x+=m
            print(x,x1)
        self.rectangle.pos=(x,y)
    def moveU(self):
        x,y=self.rectangle.pos
        w,h=self.rectangle.size
        y1=self.height-h
        if y==y1 and x==y1:
            print(y,y1)
        else:
            m=10
            y+=m
        self.rectangle.pos=(x,y)
class canvasApp(App):
    def build(self):
        return canvas_Example6()

canvasApp().run()
