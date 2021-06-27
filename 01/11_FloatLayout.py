from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class coltrol2(FloatLayout):
    def __init__(self,**kwargs):
        super(coltrol2, self).__init__(**kwargs)

        self.btn=Button(text='Button 1',size_hint=(.2,.1),pos_hint={'top':1,'x':0})
        self.btn1=Button(text='Button 2',size_hint=(.2,.1),pos_hint={'y':.5,'right':1},color=(153, 102, 255),)
        self.btn2=Button(text='Button 3',pos_hint={'top':1,'right':1},size_hint=(.2,.1))
        self.btn3=Button(text='Button 4',size_hint=(.2,.1),pos_hint={'x':0,'y':0})
        self.add_widget(self.btn)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)


class MyApp(App):
    def build(self):
        return coltrol2()
if __name__ == '__main__':
    MyApp().run()