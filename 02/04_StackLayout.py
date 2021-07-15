from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class MYStacklayout(App):
    def build(self):
        S=StackLayout()
        S.orientation='tb-rl'

        for i in range(1,11):
            i=Button(text='B%i'%i,size_hint=(.2,.1))
            S.add_widget(i)
        return S
MYStacklayout().run()