from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class myanchor(AnchorLayout):
    pass

class hibutton(BoxLayout):
    pass
class wel(BoxLayout):
    pass
class Second(BoxLayout):
    def __init__(self,**kwargs):
        super(Second, self).__init__(**kwargs)
        #self.padding=100
        b1=Button(text='A')
        self.add_widget(b1)

class First(Widget):
    pass

class myGridlayout(GridLayout):
    pass

class Boxapp(App):
    pass

Boxapp().run()
