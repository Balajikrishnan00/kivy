from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size=(305,480)


class control2(RelativeLayout):
    def __init__(self,**kwargs):
        super(control2, self).__init__(**kwargs)

        self.btn1=Button(text='R1',size_hint=(.2,.1),pos=(200,100))
        self.btn2=Button(text='R2',size_hint=(.2,.1),pos_hint={'x':.3,'y':.5})
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)



class coltrol1(App):
    def build(self):
        return control2()

if __name__ == '__main__':
    coltrol1().run()