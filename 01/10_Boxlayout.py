from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class control2(BoxLayout):
    def __init__(self,**kwargs):
        super(control2, self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding=100
        self.spacing=20
        self.btn1=Button(text='Button 1')
        self.btn2=Button(text='Button 2')
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)


class control1(App):
    def build(self):
        return control2()
if __name__ == '__main__':
    control1().run()