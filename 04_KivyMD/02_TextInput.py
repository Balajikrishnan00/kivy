from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class mycanvas(Widget):
    pass




class myimage(GridLayout):
    pass


class mybox(BoxLayout):
    textinput_text = StringProperty('Foo')

    def ontext_validate(self, widget):
        self.textinput_text = widget.text


class tesapp(App):
    pass



tesapp().run()
