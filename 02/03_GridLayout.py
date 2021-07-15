from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MYGridlayout(App):
    def build(self):
        grid=GridLayout()
        grid.cols=2
        grid.padding=30
        grid.spacing=10

        b1=Button(text='B1',size_hint=(.2,.1))
        b2 = Button(text='B2', size_hint=(.2, .1))
        b3 = Button(text='B3', size_hint=(.2, .1))
        b4 = Button(text='B4', size_hint=(.2, .1))
        b5 = Button(text='B5', size_hint=(.2, .1))
        b6 = Button(text='B6', size_hint=(.2, .1))

        grid.add_widget(b1)
        grid.add_widget(b2)
        grid.add_widget(b3)
        grid.add_widget(b4)
        grid.add_widget(b5)
        grid.add_widget(b6)

        return grid

if __name__ == '__main__':
    MYGridlayout().run()