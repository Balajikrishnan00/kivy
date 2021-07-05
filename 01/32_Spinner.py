from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label


class MyApp(App):
	def build(self):
		self.s=Spinner(text='Spinner 1',
		values=('btn1','btn2','btn3','btn4'),
		size_hint=(.2,.1))
		self.s.bind(on_press=self.show_Spinner)
		return self.s
	def show_Spinner(self,instance):
		self.text1=self.s.text
		return Label(text=f'Hello {self.text1}')
		
		
MyApp().run()