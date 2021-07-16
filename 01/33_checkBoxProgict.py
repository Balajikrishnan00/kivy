from kivy.app import App
from kivy.base import Builder

kv="""
BoxLayout:
	orientation:'vertical'
	canvas:
		Color:
			rgb:(1,1,1,1)
		Rectangle:
			pos:self.pos
			size:self.size
	CheckBox:
		group:'a'
		active:True
	CheckBox:
		id:ch2
	BoxLayout:
		Button:
			text:'Active False'
			size_y:None
			on_press:ch2.active=False
			
		Button:
			text:'Active True'
			on_press:ch2.active=True
			
			
		
"""
class M1App(App):
	def build(self):
		return Builder.load_string(kv)
M1App().run()