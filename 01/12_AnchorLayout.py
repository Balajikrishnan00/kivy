from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class control2(AnchorLayout):
    def __init__(self,**kwargs):
        super(control2, self).__init__(**kwargs)
        self.anchor_x='right'
        self.anchor_y='top'
        self.btn1=Button(text='Button 1',size_hint=(.4,.2))
        self.btn2=Button(text='Button 2',size_hint=(.2,.1),pos_hint={'x':0,'y':0})
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)






class control1(App):
    def build(self):
        return control2()
if __name__ == '__main__':
    control1().run()