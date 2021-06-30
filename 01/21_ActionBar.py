from kivy.uix.actionbar import ActionBar
from kivy.app import App
from kivy.core.window import Window
Window.size=(320,480)

class con2(ActionBar):
    def __init__(self,**kwargs):
        super(con2, self).__init__(**kwargs)
        self.pos_hint={'top':1}
        self.background_color=(6, 56, 235,1)



class con1(App):
    def build(self):
        return con2()
if __name__ == '__main__':
    con1().run()