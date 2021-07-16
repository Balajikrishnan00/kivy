from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


from kivy.uix.label import Label

class Mygrid(BoxLayout):
    #file = 'Valimai.mp3'

    def Play(self,):
        self.file_name='Valimai.mp3'

        sound=SoundLoader.load(self.file_name)

        sound.play()
        

    def Pause(self):
        pass

class SampleApp(App):
    def build(self):
        return  Mygrid()

SampleApp().run()