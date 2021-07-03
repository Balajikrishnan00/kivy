"""
from kivy.app import App
from kivy.uix.spinner import Spinner



class MyApp(App):

	def build(self):
		s=Spinner(text='Home',values=('hello',),size_hint=(.2,.1),pos_hint={'top':1})
		s.bind(on_press=self.show_value)
		return s
	def show_value(self,i):
		print('the spinner text')

if __name__ == '__main__':
	MyApp().run()
"""
from kivy.uix.spinner import Spinner

print(dir(Spinner))
help(halign)