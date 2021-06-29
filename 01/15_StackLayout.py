from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.core.window import Window

Window.size=(305,480)

class control2(StackLayout):
    def __init__(self,**kwargs):
        super(control2, self).__init__(**kwargs)
        self.orientation='rl-bt'
        self.padding=20
        self.spacing=3
        self.add_widget(Button(text='B1',size_hint=(.2,.1)))
        self.add_widget(Button(text='B2', size_hint=(.2, .1)))
        self.add_widget(Button(text='B3', size_hint=(.2, .1)))
        self.add_widget(Button(text='B4', size_hint=(.2, .1)))
        self.add_widget(Button(text='B5', size_hint=(.2, .1)))
        self.add_widget(Button(text='B6', size_hint=(.2, .1)))
        self.add_widget(Button(text='B7', size_hint=(.2, .1)))


class control1(App):
    def build(self):
        return control2()
if __name__ == '__main__':
    control1().run()


# Must be one of: ['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']