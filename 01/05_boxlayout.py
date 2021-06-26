from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.base import Builder

class MyApp(App):
    def build(self):
        b=BoxLayout(orientation='vertical',padding=(20,10),)
        b1=Button(text='Button1',background_color=(1,2,3,1))
        b2=Button(text='Button2')
        b.add_widget(b1)
        b.add_widget(b2)
        return b
if __name__ == '__main__':
    MyApp().run()
