from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.size=(384,576)


class mainwidget(Widget):
    pass

class boxlayout(BoxLayout):
    pass

class TheLabApp(App):

    def build(self):
        self.title="Mobile App"
        return mainwidget()

TheLabApp().run()