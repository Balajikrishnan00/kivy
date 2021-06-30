from kivy.app import App
from kivy.uix.button import Button

class con2(Button):
    def __init__(self,**kwargs):
        super(con2, self).__init__(**kwargs)
        self.text='HelloWorld'
        self.size_hint=(.2,.1)
        self.font_size=23
        #self.padding=(.1,.2)
        self.pos_hint={'center_x':.5,'center_y':.5}

class con1(App):
    def build(self):
        return con2()
if __name__ == '__main__':
    con1().run()