from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class control2(PageLayout):
    def __init__(self,**kwargs):
        super(control2, self).__init__(**kwargs)
        self.add_widget(Button(text='B1'))
        self.add_widget(Button(text='B2'))
        self.add_widget(Button(text='B3'))
        self.add_widget(Button(text='B4'))

class control1(App):
    def build(self):
        return control2()
if __name__ == '__main__':
    control1().run()