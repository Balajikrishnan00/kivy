from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class AudioPlay(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.padding=50
        self.spacing=30
        self.btn1=Button(text='PLAY',size_hint=(.2,.1))
        self.btn1.bind(on_press=self.Play)


        self.add_widget(self.btn1)
        self.file='Valimai.mp3'
    def Play(self,i):
        audio=SoundLoader.load(self.file)
        if audio:
            audio.play()
            self.add_widget(Label(text="Sound found at %s" % audio.source))
            self.add_widget(Label(text="Sound is %.3f seconds" % audio.length))






class mainApp(App):
    def build(self):
        return AudioPlay()
mainApp().run()