from kivy.app import App
from kivy.uix.spinner import Spinner



class MyApp(App):
	def build(self):
		s=Spinner(text='Home',values=('hello',),size_hint=(.2,.1),pos_hint={'top':1})
		return s

if __name__ == '__main__':
	MyApp().run()
