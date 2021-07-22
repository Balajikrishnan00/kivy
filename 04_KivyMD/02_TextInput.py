from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout


class myimage(GridLayout):
    pass


class mybox(BoxLayout):
    textinput_text = StringProperty('Foo')

    def ontext_validate(self, widget):
        self.textinput_text = widget.text


class tesapp(App):
    def build(self):
        return myimage()


tesapp().run()
