from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class con2(BoxLayout):
    def __init__(self,**kwargs):
        super(con2, self).__init__(**kwargs)
        self.add_widget(Label(text='[b]Welcome[/b]',markup=True,size_hint=(.2,.2),font_size=20))
        self.add_widget(Label(text='[i]Welcome[/i]',markup=True,size_hint=(.2,.2),font_size=20))
        self.add_widget(Label(text='[u]Welcome[/u]',markup=True,size_hint=(.2,.2),font_size=20))
        #self.add_widget(Label(text='[font="Lemonada-VariableFont_wght.ttf"]Welcome[/font]', markup=True, size_hint=(.2, .2), font_size=20))


class con1(App):
    def build(self):
        return con2()

if __name__ == '__main__':
    con1().run()