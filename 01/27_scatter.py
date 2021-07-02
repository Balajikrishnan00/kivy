from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.base import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class Welcome(BoxLayout):
    def __init__(self,**kwargs):
        super(Welcome, self).__init__(**kwargs)
        self.orientation='vertical'
        self.s1=Scatter(pos=(200,200))

        self.s1.add_widget(Label(text='Label1',halign='center'))
        #self.s1.add_widget(Button(text='Button1'))
        self.add_widget(self.s1)



class time(App):
    def build(self):
        return Welcome()
if __name__ == '__main__':
    time().run()
