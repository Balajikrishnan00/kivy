from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class control2(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.cols=3

        self.add_widget(Label(text='Username'))
        self.add_widget(Label(text='Hello world'))
        self.add_widget(Label(text='Username'))
        self.add_widget(Label(text='Hello world'))





class control1(App):
    def build(self):
        return control2()

if __name__ == '__main__':
    control1().run()