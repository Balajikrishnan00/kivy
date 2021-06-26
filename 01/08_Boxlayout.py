from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Second(Widget):
    pass

class firstApp(App):
    def build(self):
        return Second()

if __name__ == '__main__':
    firstApp().run()